# Validação de Nota: Peça uma nota até que ela esteja entre 0 e 10.

while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Erro: A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro: Digite um número válido.")