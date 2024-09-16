import random

# Ler arquivo:
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        palavras = [linha.strip() for linha in file if 5 <= len(linha.strip()) <= 8]
    return palavras

# Sortear a palavra:
def sortear_palavra(lista_palavras):
    return random.choice(lista_palavras)

# Feedback:
def feedback_tentativa(palavra_sorteada, tentativa):
    feedback = ''
    for letra, tentativa_letra in zip(palavra_sorteada, tentativa):
        if letra == tentativa_letra:
            feedback += '\033[92m' + letra + '\033[0m'  # verde
        elif tentativa_letra in palavra_sorteada:
            feedback += '\033[93m' + tentativa_letra + '\033[0m'  # amarelo
        else:
            feedback += '\033[90m' + tentativa_letra + '\033[0m'  # cinza
    return feedback