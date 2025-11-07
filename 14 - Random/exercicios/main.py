# 🥇 Exercício — Sorteio de Prêmios em uma Festa
# Você está organizando uma festa e tem 5 prêmios diferentes para sortear entre os convidados.

# Cada convidado só pode ganhar um único prêmio.

# Os prêmios também não podem se repetir (obviamente).

# No final, mostre qual convidado ganhou qual prêmio.

# Use as seguintes listas:

# convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
# premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

import random

convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

tamanho = len(premios) + 1

for i in range (1, tamanho):
    convidado = random.choice(convidados)
    premio = random.choice(premios)
    print(f"O convidado {convidado} recebeu o prêmio {premio}.")
    convidados.remove(convidado)
    premios.remove(premio)