# Dia da Semana: Leia um número de 1 a 7 e informe o dia correspondente.
# Caso esteja fora da faixa, informe erro.

numero = int(input("Digite um número de 1 a 7: "))

dias = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Sábado",
    7: "Domingo"
}

if numero in dias:
    print(f"Dia: {dias[numero]}")
else:
    print("Erro: Digite um número entre 1 e 7")
