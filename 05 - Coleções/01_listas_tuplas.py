# listas
alunos = ["marcos", "joão", "icaro", "icaro", "icaro"]
alunos.append("pedro") # Função que adiciona rlementos a lista
print(alunos)
alunos.remove("marcos") # Função que remove elementos da lista
print(alunos)
alunos[2] = "lucas" # substituir um valor
print(alunos)
print(len(alunos)) # tamanho da lista
alunos.insert(1, "carlos") # Insere um elemento na lista
print(alunos)
alunos.pop(0) # Reove um item levando em conta sua posição
alunos.append("ana")
alunos.sort() # Ordena em ordem alfabetica
print(alunos)
print(alunos.count("icaro")) # Conta quantas vezes um item aparece na lista

alunos2 = alunos.copy() # Se for copiar essa lista é necessário usar essa função, ou as duas listas vão ser lidas como a mesma

# tuplas
# elas são inalteráveis

talheres = ("garfo", "faca", "colher")
# talheres.pop[0] # Essa função dá erro

list = [1, 2, 3]
list.pop()
print(list)