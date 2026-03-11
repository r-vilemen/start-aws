# Soma até Digitar Zero: Leia números e some-os até que o usuário digite 0. 

soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    soma += numero
    
print(f"A soma total é: {soma}")