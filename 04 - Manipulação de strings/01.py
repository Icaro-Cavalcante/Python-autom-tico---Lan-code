nome = "Icaro"
print(nome[0]) # Retorna o caracter na posição 0
print(nome[-1]) # É possível começar pelo último caracter sando numeros negativos
print(nome[0:3]) # Retorna os caracteres de um valor ao outro
print(nome[:4]) # Vai de 0 ao número inserido
print(nome[2:]) # Começa no número inserido e vai até o final

print("-" * 20)
frase = "      olá, meu nome é Icaro       "
print(len(frase)) # Diz o tamanho da string (começa por 1)
print(frase.count("o")) # Conta quantas vezes um determinado caracter aparece
print(frase.find("n")) # Diz a posição de determinado caracter
if "icaro" in frase.lower(): # O lower deixa a string toda em minúsculo
    print("Icaro está na frase!")
else:
    print("Icaro não está na frase")

print(frase.upper()) # O upper deixa tudo maiúsculo
print(frase.capitalize()) # O capitaliza deixa a primeira letra maiúscula
print(frase.title()) # Deixa a primeira letra de todas as palavras maiúscula
print(frase.strip()) # O strip remove espaços
print(frase.replace("o", "e")) # replace substitui um caracter especifico por outro