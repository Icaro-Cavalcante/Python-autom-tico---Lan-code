import random

num = random.randint(1, 90) # Gera um número inteiro aleatório
num2 = random.uniform(1, 90) # Gera um número float aleatório
print(num)
print(num2)

frutas = ["banana", "maça", "uva"]

fruta = random.choice(frutas) # Escolhe um item aleatorio de uma lista
print(f"A fruta escolhida é {fruta}.")

comidas = ["pizza", "carne", "ovo", "feijao", "hamburguer", "pastel"]
comida = random.choices(comidas, k=3) # escolhe múltiplos items de uma lista (k é o número de items) | Temos a função sample que faz a mesma coisa, mas não permite repetição de um mesmo elemento
print(f"Coidas escolhidas {comida}")

jogos = ["kingdom hearts", "persona", "yakuza", "nier", "devil may cry"]
random.shuffle(jogos) # Deixa a ordem aleatoria
print(jogos)
