from funcao_01 import *

def main():
    quantidade = obter_valores_inteiros(1)[0] # Guarda todos os valores
    valor_minimo = obter_valores_inteiros(1)[0] # Pega o minimo valor
    valor_maximo = obter_valores_inteiros(1)[0] # Pega maximo valor 
    if quantidade > 0 and valor_minimo <= valor_maximo: # Se o variavel quantidade tem alguens valor do que zero, e valor maximo é maior do que o minimo
        sucesso, lista = gerar_lista(quantidade, valor_minimo, valor_maximo) # Guarda duas diferente variavel sucesso e lista
        if sucesso:
            nome_arquivo = input("Digite o nome do arquivo para salvar a lista: ")
            sucesso_salvar = salvar_lista(lista, nome_arquivo)
            if sucesso_salvar: # Se deu tudo certo e exxecutar embaixo
                print("Lista gerada e salva com sucesso.")
            else: # Se deu errado e executar embaixo
                print("Erro ao salvar a lista.")
        else:
            print("Erro ao gerar a lista.")
    else:
        print("Quantidade e/ou valores mínimo e máximo inválidos.")

if __name__ == "__main__":
    main()