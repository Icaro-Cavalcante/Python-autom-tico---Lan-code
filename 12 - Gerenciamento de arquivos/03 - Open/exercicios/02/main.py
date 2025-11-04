# Exercício 2 — Contador de letras
# Crie um arquivo chamado mensagem.txt com um parágrafo de texto que você inventar. Depois, escreva um script que conte e exiba quantas letras existem nesse texto.

from pathlib import Path
file = Path(r"12 - Gerenciamento de arquivos\03 - Open\exercicios\02\mensagem.txt")
file.touch()

with open (file, mode='r+', encoding='utf-8') as file:
    mensagem = file.read()

letras = 0

for letra in mensagem:
    letras+=1

print(f"A mensagem tem {letras} letras.")