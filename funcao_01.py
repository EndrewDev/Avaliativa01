import random

# Obter valores inteiros
def obter_valores_inteiros(quantidade):
    valores = []
    for i in range(quantidade):
        while True:
            try:
                valor = int(input(f"Digite o valor {i+1}: "))
                valores.append(valor)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um valor inteiro.")
    return valores

# Gera listas
def gerar_lista(quantidade, valor_minimo, valor_maximo):
    if not isinstance(quantidade, int) or not isinstance(valor_minimo, int) or not isinstance(valor_maximo, int):
        return False, None
    if quantidade <= 0 or valor_minimo > valor_maximo:
        return False, None
    lista = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]
    return True, lista

# Salvar lista
def salvar_lista(nome_lista, nome_arquivo):
    if not isinstance(nome_lista, list) or not isinstance(nome_arquivo, str):
        return False
    try:
        with open(nome_arquivo, "w") as arquivo:
            for valor in nome_lista:
                arquivo.write(str(valor) + "\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar a lista: {e}")
        return False