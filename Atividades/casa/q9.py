# Número Positivo, Negativo ou Zero: Leia um número e classifique-o.

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"{numero} é um número positivo")
elif numero < 0:
    print(f"{numero} é um número negativo")
else:
    print(f"{numero} é zero")