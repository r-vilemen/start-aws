#  Média de Vários Valores: Pergunte quantos números o usuário deseja digitar.
# Use um laço para ler esses números e calcular a média.

quantidade = int(input("Quantos números você deseja digitar? "))
soma = 0

for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    soma += numero

media = soma / quantidade
print(f"A média dos números é: {media:.2f}")