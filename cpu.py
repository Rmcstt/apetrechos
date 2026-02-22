import psutil
import time
import subprocess
import struct

# Tentar importar IOKit para acesso direto aos sensores
try:
    from Foundation import NSBundle
    IOKit = NSBundle.bundleWithIdentifier_('com.apple.framework.IOKit')
    functions = [
        ("IOServiceGetMatchingService", b"II@"),
        ("IOServiceMatching", b"@*"),
        ("IORegistryEntryCreateCFProperties", b"IIo^@II"),
        ("IOObjectRelease", b"II"),
    ]
    objc_func_ptrs = {}
    for name, sig in functions:
        objc_func_ptrs[name] = IOKit.bundleForClass_(
            IOKit).loadFunction_argumentTypes_returnValue_lazy_(name, sig[1:], sig[0:1], False)
    HAS_IOKIT = True
except:
    HAS_IOKIT = False


def obter_temperatura_iokit():
    """Tenta obter temperatura via IOKit/pyobjc"""
    if not HAS_IOKIT:
        return None
    try:
        # Procurar por sensores térmicos no IORegistry
        result = subprocess.run(
            ['ioreg', '-rc', 'AppleSmartBattery'],
            capture_output=True, text=True, timeout=2
        )
        for line in result.stdout.split('\n'):
            if 'Temperature' in line and '=' in line:
                try:
                    val = int(line.split('=')[1].strip())
                    # Temperatura da bateria em centésimos de grau
                    return val / 100.0
                except:
                    pass
    except:
        pass
    return None


def obter_temperatura():
    """Obtém temperatura do CPU no macOS M1/M2"""

    # Método 1: Tentar via IOKit
    temp = obter_temperatura_iokit()
    if temp and 20 < temp < 120:
        return temp

    # Método 2: Tentar osx-cpu-temp (funciona em Intel)
    try:
        result = subprocess.run(
            ['osx-cpu-temp'], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            temp_str = result.stdout.strip().replace('°C', '').strip()
            temp = float(temp_str)
            if temp > 0:
                return temp
    except:
        pass

    # Método 3: psutil (funciona em Linux/Windows)
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                if entries:
                    return entries[0].current
    except:
        pass

    return None


def criar_velocimetro(uso_cpu):
    tamanho_velocimetro = 12
    velocidade_atual = int(uso_cpu * tamanho_velocimetro / 100)
    velocimetro = "█" * velocidade_atual + "░" * \
        (tamanho_velocimetro - velocidade_atual)
    return f"[{velocimetro}] {uso_cpu:.1f}%"


def criar_barra_temp(temp):
    """Cria barra visual para temperatura (20-100°C range)"""
    if temp is None:
        return "[   N/A    ]  --.-°C"

    # Normalizar temp para 0-100% (considerando 20-100°C como range)
    pct = max(0, min(100, (temp - 20) / 80 * 100))
    tamanho = 10
    preenchido = int(pct * tamanho / 100)

    # Cor baseada na temperatura (via caracteres diferentes)
    if temp < 50:
        char = "▓"  # Normal
    elif temp < 70:
        char = "▓"  # Quente
    else:
        char = "█"  # Muito quente

    barra = char * preenchido + "░" * (tamanho - preenchido)
    return f"[{barra}] {temp:5.1f}°C"


def monitorar_uso_cpu():
    try:
        while True:
            # Obtém a porcentagem de uso da CPU para cada núcleo E total em uma única chamada
            uso_cpu_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)
            uso_cpu_total = sum(uso_cpu_por_nucleo) / len(uso_cpu_por_nucleo)

            # Obtém temperatura
            temp = obter_temperatura()

            # Obtém uso de memória RAM
            mem = psutil.virtual_memory()
            mem_pct = mem.percent
            mem_used = mem.used / (1024**3)  # GB
            mem_total = mem.total / (1024**3)  # GB

            # Limpa o terminal antes de imprimir a próxima atualização
            print("\033c", end="")

            # Imprime o uso de CPU para cada núcleo com barra visual
            print("╔══════════════════════════════╗")
            print("║   MONITOR DE SISTEMA - M1    ║")
            print("╠══════════════════════════════╣")

            for i, uso in enumerate(uso_cpu_por_nucleo):
                barra = "▓" * int(uso / 10) + "░" * (10 - int(uso / 10))
                print(f"║ Core {i + 1:2d}: [{barra}] {uso:5.1f}% ║")

            print("╠══════════════════════════════╣")
            # Imprime o uso total de CPU
            velocimetro = criar_velocimetro(uso_cpu_total)
            print(f"║ Total:  {velocimetro} ║")
            print("╠══════════════════════════════╣")

            # RAM
            barra_mem = "▓" * int(mem_pct / 10) + "░" * \
                (10 - int(mem_pct / 10))
            print(f"║ RAM:    [{barra_mem}] {mem_pct:5.1f}%  ║")
            print(f"║         {mem_used:.1f}GB / {mem_total:.1f}GB        ║")

            print("╚══════════════════════════════╝")

    except KeyboardInterrupt:
        print("\n\nMonitor encerrado.")


if __name__ == "__main__":
    monitorar_uso_cpu()
