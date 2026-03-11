# Separação de Pares e Ímpares: De 1 até N, armazene os pares em uma lista e os ímpares em outra.

n = int(input("Digite um número N: "))

pares = []
impares = []

for i in range(1, n + 1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")