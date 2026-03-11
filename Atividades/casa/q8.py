# Categoria por Idade: Classifique uma pessoa em:
# o Infantil (até 12)
# o Juvenil (13–17)
# o Adulto (18–59)
# o Idoso (60+)

age = int(input("Digite a idade: "))

if age <= 12:
    print("Infantil")
elif age <= 17:
    print("Juvenil")
elif age <= 59:
    print("Adulto")
else:
    print("Idoso")