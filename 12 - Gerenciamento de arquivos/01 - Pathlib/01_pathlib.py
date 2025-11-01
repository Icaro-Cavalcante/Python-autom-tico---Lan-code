from pathlib import Path

caminho = Path(r"12 - Gerenciamento de arquivos/01 - Pathlib/mensagem.txt") # Caminho relativo
print(caminho)
absolute = Path(r"C:\Users\anail\OneDrive\Documentos\Códigos\dvdvd\Python-autom-tico---Lan-code\12 - Gerenciamento de arquivos\01 - Pathlib\mensagem.txtt") # Caminho absoluto
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

caminho = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\mensagem.txt")
texto = caminho.read_text() # lê texto
print(texto)

caminho.write_text("Python é legal.", encoding="utf-8") # Escreve texto no arquivo | enconding="utf-8" para aceitar caracteres especiais

pasta = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\pasta")
pasta = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib")
# for file in pasta.iterdir():
#     print(file)
for file in pasta.glob("*.txt"): # filtra pelo tipo do arquivo
    print(file)

caminho = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\01_pathlib.py")
print("-" * 20)
print(caminho) # caminho
print(caminho.name) # nome completo
print(caminho.stem) # nome sem o sufixo
print(caminho.suffix) # sufixo

caminho = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\arquivo.txt")
caminho.touch() # cria o arquivo