import time
import os

def caveira():
    print("  _._     _,-'""`-._")
    print(" (,-.`._,'(       |\`-/|")
    print("     `-.-' \ )-`( , o o)")
    print("           `-    \`_`"'-')

def caveira2():
    print("       _.__,-'""`-._")
    print(" ('._,',-.(       |\`-/|")
    print("  `-.-'    \ )-`( , o o)")
    print("           `-    \`_`"'-')

def caveira3():
    print("  _._     _,-'""`-._")
    print(" (,-.`._,'(       |\`-/|")
    print("     `-.-' \ )-`( , - -)")
    print("           `-    \`_`"'-')

def time_sleep():
    time.sleep(0.3)

def animacao_caveira():
    while True:
        # Limpa o terminal antes de imprimir a próxima caveira
        caveira()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira2()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira2()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira2()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira3()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira2()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira2()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira2()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")
        caveira3()
        time_sleep()
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    try:
        animacao_caveira()
    except KeyboardInterrupt:
        print("\nAnimação da caveira encerrada.")