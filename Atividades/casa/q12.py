# Tabuada: Leia um número e mostre sua tabuada de 1 a 10.

numero = int(input("Digite um número: "))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")