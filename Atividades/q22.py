# Jogo da Adivinhação: Gere um número aleatório e peça ao usuário para adivinhar até acertar.

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Pensei em um número entre 1 e 100. Tente adivinhar!")
    
    while not acertou:
        try:
            palpite = int(input("\nDigite seu palpite: "))
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            
            tentativas += 1
            
            if palpite < numero_secreto:
                print("O número é maior!")
            elif palpite > numero_secreto:
                print("O número é menor!")
            else:
                acertou = True
                print(f"\n🎉 Parabéns! Você acertou em {tentativas} tentativa(s)!")
        
        except ValueError:
            print("Digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()