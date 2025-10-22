# Crie um menu com 3 opções:
# 1. Pizza
# 2. Sushi
# 3. Salada

# O usuário digita um número. O programa mostra o prato escolhido.
# Se digitar qualquer outro número, exiba: "Opção inválida."

comida = int(input("1 - Pizza \n2 - Sushi \n3 - Salada \nSelecione uma comida do menu: "))
print("-" * 20)
match comida:
    case 1:
        print("Aqui está sua pizza")
    case 2:
        print("Aqui está seu sushi")
    case 3:
        print("Aqui está sua salada")
    case _:
        print("Opção inválida")