# Validação de Login: Compare usuário e senha digitados com valores prédefinidos.
# Informe se o acesso foi permitido ou negado.


USUARIO_CORRETO = "admin"
SENHA_CORRETA = "senha123"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("Acesso permitido!")
else:
    print("Acesso negado!")