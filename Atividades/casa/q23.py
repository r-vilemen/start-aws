# Caixa Registradora: Leia valores de produtos até o usuário digitar 0. Mostre o total ao final.

total = 0

while True:
    valor = float(input("Digite o valor do produto (0 para sair): "))
    
    if valor == 0:
        break
    
    total += valor

print(f"Total: R$ {total:.2f}")