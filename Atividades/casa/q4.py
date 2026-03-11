#  Classificação de Nota: Leia uma nota de 0 a 10 e informe:
# o Aprovado (≥ 7)
# o Recuperação (≥ 5 e < 7)
# o Reprovado (< 5)

nota = float(input("Digite a nota (0 a 10): "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")