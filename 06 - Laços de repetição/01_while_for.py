# while
def enquanto():
    num = 0
    while num <= 3:
        print(f"Número {num}")
        num+=1

    user = "none"
    while user.lower() != "icaro":
        user = str(input("Digite seu usuário: "))
    print(f"Bem vindo {user}")

# enquanto()

# for

for num in range (1,8 + 1):
    print(f"Número {num}")

legumes = ["tomate", "alface", "cenoura"]
for legume in legumes:
    num = legumes.index(legume) + 1
    print(f"legume {num}: {legume}")

print("-" * 20)

def par_impar(x,y):
    for num in range(x, y + 1):
        if num % 2 == 0:
            print(f"{num} é par")
        else:
            print(f"{num} é ímpar")

par_impar(-10, 40)