import platform
import psutil

def get_system_info():
    # Informações do sistema operacional
    os_info = platform.uname()
    print("Sistema Operacional:")
    print(f"  Nome: {os_info.system}")
    print(f"  Versão: {os_info.version}")
    print(f"  Arquitetura: {os_info.machine}")
    print(f"  Processador: {os_info.processor}")
    print()

    # Informações sobre a CPU
    cpu_info = platform.processor()
    print("Informações da CPU:")
    print(f"  Processador: {cpu_info}")
    print(f"  Núcleos Físicos: {psutil.cpu_count(logical=False)}")
    print(f"  Núcleos Lógicos: {psutil.cpu_count(logical=True)}")
    print()

    # Informações sobre a memória
    mem_info = psutil.virtual_memory()
    print("Informações da Memória:")
    print(f"  Memória Total: {get_size(mem_info.total)}")
    print(f"  Memória Disponível: {get_size(mem_info.available)}")
    print(f"  Memória Usada: {get_size(mem_info.used)}")
    print(f"  Porcentagem de Uso: {mem_info.percent}%")
    print()

    # Informações sobre o disco
    disk_info = psutil.disk_usage("/")
    print("Informações do Disco:")
    print(f"  Espaço Total: {get_size(disk_info.total)}")
    print(f"  Espaço Disponível: {get_size(disk_info.free)}")
    print(f"  Espaço Usado: {get_size(disk_info.used)}")
    print(f"  Porcentagem de Uso: {disk_info.percent}%")

def get_size(bytes, suffix="B"):
    # Função auxiliar para converter bytes em formato legível
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(bytes) < 1024.0:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= 1024.0
    return f"{bytes:.2f} Y{suffix}"


if __name__ == "__main__":
    get_system_info()

