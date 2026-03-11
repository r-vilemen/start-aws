# Menu até Sair: Mostre um menu e repita até o usuário escolher sair. 

while True:
    print("\n=== MENU ===")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("0. Sair")
    
    escolha = input("\nEscolha uma opção: ")
    
    if escolha == "1":
        print("Você escolheu a opção 1")
    elif escolha == "2":
        print("Você escolheu a opção 2")
    elif escolha == "3":
        print("Você escolheu a opção 3")
    elif escolha == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")