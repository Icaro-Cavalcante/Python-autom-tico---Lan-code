# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).

# Quando o usuário digitar 0, o programa para e mostra o total economizado.

cofrinho = 0
while True:
    dinheiro = int(input("Quanto deseja colocar no cofrinho? R$"))
    cofrinho+= dinheiro
    if dinheiro == 0:
        print(f"Você economizou: R${cofrinho}")
        break