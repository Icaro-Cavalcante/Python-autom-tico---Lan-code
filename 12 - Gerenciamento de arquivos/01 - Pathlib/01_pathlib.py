from pathlib import Path

caminho = Path("12 - Gerenciamento de arquivos/01 - Pathlib/mensagem.txt") # Caminho relativo
print(caminho)
absolute = Path(r"/homeyora/Documentos/GitHub/Python-autom-tico---Lan-code/12 - Gerenciamento de arquivos/01 - Pathlib/mensagem.txt") # Caminho absoluto
absolute = caminho.absolute() # Podemos transformar um caminho relativo em absoluto

if caminho.exists: # verifica se existe
    print("O caminho existe")
else:
    print("O caminho não existe")

print(absolute)

# caminho = Path("12 - Gerenciamento de arquivos/01 - Pathlib/pasta")

if caminho.is_file(): # verifica se é um arquivo
    print("é um arquivo")
elif caminho.is_dir(): # verifica se e uma pasta
    print("é uma pasta")

# nova_pasta = Path("nova_pasta/pasta2/pasta3")

nova_pasta = Path("nova_pasta")

nova_pasta.mkdir(exist_ok=True, parents=True) # make dir (fazer pasta) | o (exist_ok="True") só cria a pasta se ela não existir para evitar que dê erro | o parents=True permite a criação de multiplas pastas

# caminho.unlink() # Remove arquivos
nova_pasta.rmdir() # Remove pastas

caminho = Path("mensagem.txt")
texto = caminho.read_text()
print(texto)

caminho.write_text("Python")