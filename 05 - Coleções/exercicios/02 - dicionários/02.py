# Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
# Depois, verifique se a idade é maior ou igual a 18:

# Se sim, imprima: "Acesso liberado para {nome}"

# Se não, imprima: "Acesso negado para {nome}"

nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))

usuario = {

}
usuario["nome"] = nome
usuario["idade"] = idade
print(usuario)

if usuario["idade"] >= 18:
    print(f"Acesso liberado para {nome}")
else:
    print(f"Acesso negado para {nome}")