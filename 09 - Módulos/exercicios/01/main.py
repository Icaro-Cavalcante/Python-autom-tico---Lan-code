# Desafio 1 – Separando funções por categoria
# Crie um arquivo matematica.py com as funções:

# dobro(numero) → retorna o dobro

# metade(numero) → retorna a metade

# Crie outro arquivo mensagens.py com a função:

# boas_vindas(nome) → imprime uma mensagem de saudação

# No arquivo principal (main.py):

# Importe as funções dos dois arquivos

# Peça ao usuário um número e mostre o dobro e a metade

# Dê boas-vindas usando o nome digitado

import modulos
from modulos.matematica import *
from modulos.mensagens import *

num = int(input("Informe um número: "))
dobro = dobro(num)
metade = metade(num)
print(f"Dobro: {dobro}, Metade: {metade}")
nome = str(input("Diga seu nome: "))
boas_vindas(nome)