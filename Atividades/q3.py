# Comparação de Dois Números: Leia dois números e informe qual é o maior, ou se são iguais
# import os
# import sys

num1 = int(input("Informe um número:"))
num2 = int(input("Informe outro número:"))

if num1 == num2:
    print("Os números são iguais!.")
elif num1 > num2:
    print("O primeiro número é maior que o segundo.")
elif num1 < num2:
    print("O segundo número é maior que o primeiro.")

# opcao = input("Deseja reiniciar o programa? (s/n):")

# if opcao.lower() == "s":
#     os.execv(sys.executable,
# [sys.executable] + sys.argv)

# print("fim do programa")