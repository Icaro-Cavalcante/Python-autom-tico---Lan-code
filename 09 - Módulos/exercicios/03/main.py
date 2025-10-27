# Desafio 3 – Mini sistema de perfil de usuário
# Estrutura esperada:

# perfil/
# ├── usuario.py
# ├── validacao.py
# main.py

# usuario.py → função criar_perfil(nome, idade) → retorna dicionário com os dados
# validacao.py → função idade_valida(idade) → retorna True se idade >= 18

# main.py →

# Recebe os dados do usuário
# Valida a idade
# Se for válida, cria e exibe o perfil
# Senão, exibe uma mensagem de acesso negado

from perfil.usuario import *
from perfil.validacao import *

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))

valido = idade_valida(idade)
if valido:
    perfil = criar_perfil(nome, idade)
    print(f"Nome: {perfil["nome"]}\nIdade: {perfil["idade"]}")
else:
    print("Acesso negado!")