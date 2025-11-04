# Exercício 3 — Filtrando logs por palavra-chave
# Baixe o arquivo logs.txt anexado, e escreva um programa que:

# Leia todas as linhas do arquivo

# Peça ao usuário uma palavra-chave (como ERROR, INFO, WARNING, etc...)

# Mostre apenas as linhas que contenham essa palavra-chave.

log = (r"12 - Gerenciamento de arquivos\03 - Open\exercicios\03\acesso.log")

with open(log, mode="r+", encoding='utf-8') as file:
    log = file.read()
    # log = file.readlines() | Poderia ter usado essa função no lugar de splitlines
log = log.splitlines()

chave = str(input("Digite uma palavra-chave: "))

for linha in log:
    if chave.upper() in linha:
        print(linha)