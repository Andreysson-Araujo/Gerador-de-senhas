#ideia de transferir o codigo abaixo para uma interface

from random import choice
import string

tamanho = 12

caracteres = string.ascii_letters + string.digits + string.punctuation

while True:
    c=0
    senha = ""
    while c < tamanho:
        senha += choice(caracteres)
        c +=1
    if tamanho == 12:
        break

print(f"Sua senha é {senha}")
