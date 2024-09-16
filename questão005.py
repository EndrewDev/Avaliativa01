from funcao_05 import *

def main():
    origem = input("Digite o nome do arquivo de origem: ")
    palavra_passe = input("Digite a palavra-passe: ")
    destino = input("Digite o nome do arquivo de destino: ")

    xor_encrypt(origem, palavra_passe, destino)
    print(f"Operação concluída. Resultado salvo em {destino}.")

if __name__ == "__main__":
    main()