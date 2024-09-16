from funcao_02 import *

def ler_arquivo(nome_arquivo): # Função para ler o arquivo
    try:
        with open(nome_arquivo, 'r') as file:
            lista = [int(line.strip()) for line in file]
        return True, lista
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return False, None
    except Exception as e: # se der errado executa embaixo
        print(f"Erro ao ler arquivo: {e}")
        return False, None

def solicitar_nome_arquivo(): # funcao para solicitar nome do arquivo
    while True:
        nome_arquivo = input("Digite o nome do arquivo: ")
        if nome_arquivo.strip() != "":
            return nome_arquivo


nome_arquivo = solicitar_nome_arquivo()

# Ler arquivo:
sucesso_leitura, lista = ler_arquivo(nome_arquivo)
if sucesso_leitura:
    print("Lista lida do arquivo:", lista)

    metodo_ordena = input("Escolha o método de ordenação (BUBBLE, INSERTION, SELECTION ou QUICK): ").upper()

    # Ordenar lista:
    if metodo_ordena == "BUBBLE":
        sucesso_ordena, lista_ordenada = ordena_bubble(lista)
    elif metodo_ordena == "INSERTION":
        sucesso_ordena, lista_ordenada = ordena_insertion(lista)
    elif metodo_ordena == "SELECTION":
        sucesso_ordena, lista_ordenada = ordena_selection(lista)
    elif metodo_ordena == "QUICK":
        sucesso_ordena, lista_ordenada = ordena_quick(lista)
    else:
        print("Erro: Método de ordenação inválido.")
        sucesso_ordena, lista_ordenada = False, None

    if sucesso_ordena:
        print("Lista ordenada:", lista_ordenada)
    else:
        print("Erro ao ordenar a lista.")
else:
    print("Erro ao ler o arquivo.")