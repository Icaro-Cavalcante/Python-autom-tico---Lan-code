arquivo = (r"12 - Gerenciamento de arquivos\03 - Open\arquivo.txt")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close() # Sempre bom fechar o arquivo

# Com o with open, ele fecha no final do código

# with open(r"12 - Gerenciamento de arquivos\03 - Open\arquivo.txt") as arquivo:
#     print(arquivo.read())


# mode 'w' substitui o texto

# with open(arquivo, mode='w', encoding='utf-8') as file:
#     file.write("Olá pessoas.")

# mode 'a' adiciona ao texto

# with open(arquivo, mode='a', encoding='utf-8') as file:
#     file.write("Olá pessoas.")

# mode 'r+' lê e escreve

with open(arquivo, mode='r+', encoding='utf-8') as file:
     file.write("Olá pessoas.\n")
     file.seek(0) # resetar a posição do ponteiro
     print(file.read())