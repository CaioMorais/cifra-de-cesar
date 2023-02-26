#Caio de Morais Costa - 082180015
#João Guilherme Cabral - 082180011
#Junior Freitas - 082180035
#Wagner Olimpio - 082180033

#Todo o código foi gerado pelo ChatGPT

import shutil

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇabcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüç'

def encrypt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    encrypted_text = ''
    for char in text:
        if char in ALFABETO:
            index = ALFABETO.index(char)
            encrypted_index = (index + 3) % len(ALFABETO)
            encrypted_text += ALFABETO[encrypted_index]
        else:
            encrypted_text += char
    with open(file_path + '.enc', 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

def decrypt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    decrypted_text = ''
    for char in text:
        if char in ALFABETO:
            index = ALFABETO.index(char)
            decrypted_index = (index - 3) % len(ALFABETO)
            decrypted_text += ALFABETO[decrypted_index]
        else:
            decrypted_text += char
    with open(file_path + '.dec', 'w', encoding='utf-8') as file:
        file.write(decrypted_text)

# Criptografar arquivo
encrypt_file('arquivo.txt')

# Fazer backup do arquivo original
shutil.copy('arquivo.txt', 'arquivo.txt.bkp')

# Descriptografar arquivo
decrypt_file('arquivo.txt.enc')

input('Para resgatar seus dados, transfira 1 milhão de libras para o pix 43091845632')