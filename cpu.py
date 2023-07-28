import psutil
import time

def criar_velocimetro(uso_cpu):
    tamanho_velocimetro = 10
    velocidade_atual = int(uso_cpu * tamanho_velocimetro / 20)
    velocimetro = "⌨︎" * velocidade_atual + "-" * (tamanho_velocimetro - velocidade_atual)
    return f"[{velocimetro}] \n M1   {uso_cpu:.1f}%"

def monitorar_uso_cpu():
    while True:
        # Obtém a porcentagem de uso da CPU para cada núcleo
        uso_cpu_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)

        # Obtém a porcentagem de uso total da CPU
        uso_cpu_total = psutil.cpu_percent(interval=1)
		

        # Limpa o terminal antes de imprimir a próxima atualização
        print("\033c", end="")

        # Imprime o uso de CPU para cada núcleo
        for i, uso in enumerate(uso_cpu_por_nucleo):
            print(f"core {i + 1}: {uso:.1f}%")

        print('')
        # Imprime o uso total de CPU
        velocimetro = criar_velocimetro(uso_cpu_total)
        print(velocimetro)

if __name__ == "__main__":
    monitorar_uso_cpu()

