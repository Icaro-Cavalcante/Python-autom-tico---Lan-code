# 3. Automatizando extração de arquivos
# Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:

# Crie uma pasta chamada extraido/.

# Extraia o conteúdo do .zip dentro da pasta criada.

# Ao final, liste todos os arquivos extraídos.

from pathlib import Path
import shutil

zip = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\03\arquivos_secretos.zip")
extraido = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\03\extraido")
shutil.unpack_archive(zip, extraido)

for file in extraido.iterdir():
    print(file.name)