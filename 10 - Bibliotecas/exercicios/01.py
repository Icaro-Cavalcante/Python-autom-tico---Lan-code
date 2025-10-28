# Exercício – Jogo de Adivinhação 🎯
# Crie um programa que sorteia um número inteiro entre 1 e 10 usando a biblioteca random.
# O jogador tem que tentar adivinhar esse número.
# O jogo deve continuar perguntando até o jogador acertar.

# A cada tentativa, o programa deve informar:

# "Muito alto!" se o palpite for maior que o número sorteado
# "Muito baixo!" se for menor
# "Acertou!" se for igual

# Ao final, informe quantas tentativas foram necessárias para acertar.

import random

aleatorio = random.randint(1, 10)
tentativas = 0

while True:
    tentativas += 1
    print("-" * 20)
    num = int(input("Tente adivinhar um número de 0 a 10: "))
    if num == aleatorio:
        print("Acertou!")
        break
    elif num < aleatorio:
        print("Muito baixo!")
    elif num > aleatorio:
        print("Acertou!")
print("-" * 20)
print(f"Você acertou o número com {tentativas} tentativa/s.")
