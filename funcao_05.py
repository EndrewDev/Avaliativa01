def xor_encrypt(origem, palavra_passe, destino):
    with open(origem, 'rb') as origem_file:
        with open(destino, 'wb') as destino_file:
            palavra_passe_bytes = [ord(char) for char in palavra_passe]
            palavra_passe_len = len(palavra_passe_bytes)
            index = 0

            while True:
                byte = origem_file.read(1)
                if not byte:
                    break

                # Realiza a operação de XOR com o próximo byte da palavra-passe:
                byte_cifrado = byte[0] ^ palavra_passe_bytes[index]
                destino_file.write(bytes([byte_cifrado]))

                # Atualiza o índice da palavra-passe para o próximo byte:
                index = (index + 1) % palavra_passe_len