# O que seu programa deve fazer:
# Exibir um menu com as opções:

# 1. Adicionar aluno

# 2. Listar todos os alunos

# 3. Buscar aluno pelo nome

# 4. Remover aluno

# 5. Mostrar média geral das notas

# 6. Sair

# ✏️ Funcionalidades detalhadas:
# ➕ Adicionar aluno
# Pedir o nome, a idade e a nota (0 a 10) do aluno.

# Salvar os dados em um dicionário.

# Adicionar o dicionário a uma lista de alunos.

# 📋 Listar todos os alunos
# Mostrar todos os alunos cadastrados com nome, idade e nota.

# Exibir mensagem se não houver nenhum aluno.

# 🔍 Buscar aluno pelo nome
# Perguntar um nome e procurar na lista.

# Exibir os dados se o aluno for encontrado.

# Se não existir, exibir uma mensagem de erro.

# 🗑️ Remover aluno
# Perguntar o nome do aluno.

# Se existir, remover da lista.

# Se não existir, exibir aviso.

# 📊 Média geral das notas
# Calcular e exibir a média de todas as notas dos alunos cadastrados.

# Se não houver alunos, exibir uma mensagem adequada.

# ✅ Requisitos técnicos:
# Usar listas e dicionários para armazenar os dados.

# Separar funcionalidades em funções.

# Usar um loop principal com menu (while True) para manter o programa rodando até o usuário sair.

# Validar entradas (por exemplo: nota deve ser um número entre 0 e 10).

alunos = {
    "nomes": ["icaro", "joao"],
    "idades": [18, 17],
    "notas": [7, 8]
}

def Adicionar():
        print("-" * 20)
        nome = str(input("Qual o nome do aluno? "))
        idade = int(input("Qual a idade do aluno? "))
        while True:
            nota = float(input("Qual a nota do aluno? "))
            if nota > 10 or nota < 0:
                print("Insira uma nota válida")
            else:
                 alunos["nomes"].append(nome.lower())
                 alunos["idades"].append(idade)
                 alunos["notas"].append(nota)
                 print(f"O aluno {nome} foi cadastrado com sucesso")
                 break

def Listar():
    print("-" * 20)
    for nome in alunos["nomes"]:
        index = alunos["nomes"].index(nome)
        print(f"Nome: {alunos['nomes'][index]} Idade: {alunos['idades'][index]} Nota: {alunos['notas'][index]}")

def Buscar():
    print("-" * 20)
    busca = str(input("Que aluno deseja buscar? "))
    if busca.lower() in alunos["nomes"]:
        index = alunos["nomes"].index(busca.lower())
        print(f"Nome: {alunos['nomes'][index]} Idade: {alunos['idades'][index]} Nota: {alunos['notas'][index]}")
    else:
         print(f"Aluno {busca} não foi encontrado.")

def Remover():
    print("-" * 20)
    remover = str(input("Que aluno deseja remover? "))
    if remover.lower() in alunos["nomes"]:
        index = alunos["nomes"].index(remover.lower())
        alunos["nomes"].pop(index)
        alunos["idades"].pop(index)
        alunos["notas"].pop(index)
        print(f"O aluno {remover} foi removido.")
    else:
         print(f"Aluno {remover} não foi encontrado.")
    
def Media():
    print("-" * 20)
    soma = 0
    for nota in alunos["notas"]:
          soma += nota
    media = soma / (len(alunos["notas"]))
    print(f"A média geral é: {media}")

while True:
    print("-" * 20)
    print("Sistema de alunos")
    print("-" * 20)
    print("1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair")
    escolha = int(input("Qual a sua escolha? "))
    if escolha == 1:
        Adicionar()
    elif escolha == 2:
        Listar()
    elif escolha == 3:
        Buscar()
    elif escolha == 4:
        Remover()
    elif escolha == 5:
        Media()
    elif escolha == 6:
        break
    else:
        print("Escolha inválida.")