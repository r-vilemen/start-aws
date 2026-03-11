# Desconto em Compra: Leia o valor de uma compra.
# o Se for maior que 200, aplique 15% de desconto.
# o Caso contrário, aplique 5%.

valor = float(input("Digite o valor da compra: "))

if valor > 200:
    desconto = valor * 0.15
else:
    desconto = valor * 0.05

valor_final = valor - desconto

print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")