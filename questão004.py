from funcao_04 import *

# Jogar:
def jogar(palavra_sorteada):
    tentativas = 6
    tentativa_atual = ''

    while tentativas > 0:
        tentativa_atual = input(f"Tentativa {7 - tentativas} de 6. Digite a palavra ({len(palavra_sorteada)} letras): ")

        if len(tentativa_atual) != len(palavra_sorteada): # Se a palavra for errada
            print(f"A palavra deve ter {len(palavra_sorteada)} letras. Tente novamente.")
            continue

        if tentativa_atual == palavra_sorteada: # Se a palavra for certa
            print(f"Parabéns! Você acertou a palavra '{palavra_sorteada}' em {6 - tentativas + 1} tentativas.")
            return

        feedback = feedback_tentativa(palavra_sorteada, tentativa_atual)
        print("Feedback:", feedback)
        tentativas -= 1

    print(f"Você perdeu! A palavra correta era '{palavra_sorteada}'.")

def main():
    nome_arquivo = "lista_palavras.txt"
    palavras = ler_arquivo(nome_arquivo)

    if palavras: # Quantas letras tem
        palavra_sorteada = sortear_palavra(palavras)
        print(f"A palavra sorteada tem {len(palavra_sorteada)} letras.")

        jogar(palavra_sorteada)
    else: # Se a palavra vazia ou não encontrado
        print("Erro: Lista de palavras vazia ou arquivo não encontrado.")

if __name__ == "__main__":
    main()