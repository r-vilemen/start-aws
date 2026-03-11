# Par ou Ímpar: Leia um número inteiro e informe se ele é par ou ímpar.
# import os
# import sys

num = int(input("Digite um número:"))

if num % 2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"o número {num} é ímpar!")










# opcao = input("Deseja reiniciar o programa? (s/n):")

# if opcao.lower() == "s":
#     os.execv(sys.executable,
# [sys.executable] + sys.argv)

# print("fim do programa")

# - sys.executable pega o caminho do Python que está rodando o Script
# - sys.argv mantém os mesmos argumentos do terminal
# - os.execv substitui o processo atual por um novo, como se tivesse digitado novamente no terminal