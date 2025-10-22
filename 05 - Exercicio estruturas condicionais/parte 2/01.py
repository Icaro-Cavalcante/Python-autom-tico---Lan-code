# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:
# Nota 9 ou 10: "Excelente!"
# Nota 7 ou 8: "Muito bom"
# Nota 5 ou 6: "Regular"
# Menor que 5: "Ruim"

nota = int(input("Dê uma nota para o filme: "))

while nota not in range(1,11):
    print("A nota precisar ser entre 1 e 10")
    print("-" * 50)
    nota = int(input("Dê uma nota para o filme: "))

if nota == 9 or nota == 10:
    print("Excelente!")
elif nota == 7 or nota == 8:
    print("Muito nom")
elif nota == 5 or nota == 6:
    print("Regular")
elif nota < 5:
    print("Ruim")