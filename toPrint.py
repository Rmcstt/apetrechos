def colocar_em_print(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(f'print("{linha.strip()}")')
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    arquivo_txt = "clippy.txt"
    colocar_em_print(arquivo_txt)
