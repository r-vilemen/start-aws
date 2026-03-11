# Temperatura da Água: Leia uma temperatura e informe se a água estaria:
# o Sólida (≤ 0)
# o Líquida (entre 0 e 100)
# o Gasosa (> 100)

temperatura = float(input("Informe a temperatura da água em °C: "))

if temperatura <= 0:
    estado = "Sólida"
elif temperatura < 100:
    estado = "Líquida"
else:
    estado = "Gasosa"

print(f"A água está {estado}")