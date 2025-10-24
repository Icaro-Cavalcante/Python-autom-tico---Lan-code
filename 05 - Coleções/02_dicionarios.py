pessoa = {
    "nome":"icaro",
    "idade": 18,
    "genero": "masculino",
    "altura": 1.62,
    "conhecimentos": ["programação", "desenho", "ingles"]
}
pessoa["idade"] = 19
print(pessoa["idade"])
print(pessoa["conhecimentos"][0])
print(pessoa.keys()) # mostra as chaves do dicionário
print(pessoa.values()) # mostra os valores do dicionário
print(pessoa.items()) # mostra os items do dicionário

print("-" * 20)
print(pessoa.get('nome', "nome não existe"))
item_removido = pessoa.pop('genero')
print(f"Item removido: {item_removido}\n{pessoa}")