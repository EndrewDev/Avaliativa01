from funcao_03 import *

def display_choices(texts_bits):
    print("Escolha uma opção para preencher a tabela:")
    for idx, (text, bits) in enumerate(texts_bits, start=1):
        print(f"{idx}. Texto: '{text}' | Bits em zero: {bits}")

    choice = int(input("Digite o número da opção desejada: "))
    if choice < 1 or choice > len(texts_bits):
        print("Opção inválida. Por favor, escolha um número válido.")
        return None
    return texts_bits[choice - 1]

# Defina o texto e os bits em zero para a tabela
texts_bits = [
    ("Esse é fácil", 8),
    ("Esse é fácil", 10),
    ("Esse é fácil", 15),
    ("Texto maior muda o tempo?", 8),
    ("Texto maior muda o tempo?", 10),
    ("Texto maior muda o tempo?", 15),
    ("É possível calcular esse?", 18),
    ("É possível calcular esse?", 19),
    ("É possível calcular esse?", 20)
]

# Exibir opções e obter informações do usuário
chosen_option = display_choices(texts_bits)
if chosen_option:
    text, bits = chosen_option
    data_to_hash = text.encode('utf-8')
    nonce, time_taken = findNonce(data_to_hash, bits)
    print(f"\nTexto a validar: '{text}'")
    print(f"Bits em zero: {bits}")
    print(f"Nonce encontrado: {nonce}")
    print(f"Tempo (em s) para encontrar o nonce: {time_taken:.6f}")
else:
    print("Programa encerrado.")