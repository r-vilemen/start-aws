# Criação de Senha Segura: Solicite uma senha até que ela tenha: 
# • Pelo menos 6 caracteres;
# • Pelo menos 1 número;
# • Pelo menos 1 letra;

import re

while True:
    senha = input("Digite uma senha: ")
    
    if len(senha) < 6:
        print("Erro: A senha deve ter pelo menos 6 caracteres.")
        continue
    
    if not re.search(r'\d', senha):
        print("Erro: A senha deve conter pelo menos 1 número.")
        continue
    
    if not re.search(r'[a-zA-Z]', senha):
        print("Erro: A senha deve conter pelo menos 1 letra.")
        continue
    
    print("Senh válida!")
    break