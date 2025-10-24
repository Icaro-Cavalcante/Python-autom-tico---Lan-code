# Exercício 2 – Manipulando uma lista
# Dada a lista abaixo:

# livros = ["Python", "Java", "C++"]
# Realize as seguintes ações:

# Adicione o livro "JavaScript"

# Remova o livro "Java"

# Troque "Python" por "Go"

# Mostre o tamanho da lista
livros = ["Python", "Java", "C++"]
livros.append("JavaScript")
livros.remove("Java")
livros[livros.index("Python")] = "Go"
print(f"Tamanho: {len(livros)}\nLista: {livros}")