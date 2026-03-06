# Contar Divisores: Leia um número e conte quantos divisores ele possui.

num = int(input("Digite um número: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print(f"O número {num} possui {count} divisores")