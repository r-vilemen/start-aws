# Maioridade: Leia a idade de uma pessoa e informe se ela é maior ou menor deidade.

idade = (input("Digite sua Idade:"))

if isinstance(idade, (int)):
    if idade >= 18:
        print("Você é de MAIOR idade.")
    elif idade >= 0 and idade < 18:
        print("Você é de MENOR idade.")
    else:
        print("Idade Inválida!")

elif not isinstance(idade, int):
    print("Idade Inválida!")
else:
    print("Idade Inválida!")
