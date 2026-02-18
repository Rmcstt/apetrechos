import psutil
import time


def criar_velocimetro(uso_cpu):
    tamanho_velocimetro = 12
    velocidade_atual = int(uso_cpu * tamanho_velocimetro / 100)
    velocimetro = "█" * velocidade_atual + "░" * \
        (tamanho_velocimetro - velocidade_atual)
    return f"[{velocimetro}] {uso_cpu:.1f}%"


def monitorar_uso_cpu():
    try:
        while True:
            # Obtém a porcentagem de uso da CPU para cada núcleo E total em uma única chamada
            uso_cpu_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)
            uso_cpu_total = sum(uso_cpu_por_nucleo) / len(uso_cpu_por_nucleo)

            # Limpa o terminal antes de imprimir a próxima atualização
            print("\033c", end="")

            # Imprime o uso de CPU para cada núcleo com barra visual
            print("╔══════════════════════════════╗")
            print("║     MONITOR DE CPU - M1      ║")
            print("╠══════════════════════════════╣")

            for i, uso in enumerate(uso_cpu_por_nucleo):
                barra = "▓" * int(uso / 10) + "░" * (10 - int(uso / 10))
                print(f"║ Core {i + 1:2d}: [{barra}] {uso:5.1f}% ║")

            print("╠══════════════════════════════╣")
            # Imprime o uso total de CPU
            velocimetro = criar_velocimetro(uso_cpu_total)
            print(f"║ Total:  {velocimetro} ║")
            print("╚══════════════════════════════╝")

    except KeyboardInterrupt:
        print("\n\nMonitor encerrado.")


if __name__ == "__main__":
    monitorar_uso_cpu()
