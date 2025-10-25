# Crie um sistema de votação onde o usuário escolhe entre:

# 1."Pizza"
# 2."Hambúrguer"
# 3."Sair"

# Enquanto ele não digitar "3", continue perguntando
# No final, mostre quantos votos cada item recebeu

pizza = 0
hamburguer = 0

while True:
    print("-"*20)
    print("Votação")
    print("-"*20)
    print("Escolha um:\n1 - pizza\n2 - Hambúrguer\n3 - Sair")
    escolha = int(input("Escolha: "))
    if escolha == 1:
        pizza+= 1
    elif escolha == 2:
        hamburguer+= 1
    elif escolha== 3:
        print("-"*20)
        print(f"Votos:\nPizza - {pizza}\nHambúrguer - {hamburguer}")
        break
    else:
        print("Escolha inválida")