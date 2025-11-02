# 1. Cópia simples com estrutura
# Crie um script que:

# Crie uma pasta imagens.

# Coloque 2 arquivos fictícios .png dentro dela

# Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup.

from pathlib import Path
import shutil

imagens = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\01\imagens")
backup = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\01\backup")
imagens.mkdir(exist_ok=True)

foto1 = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\01\imagens\foto1.png")
foto2 = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\01\imagens\foto2.png")

foto1.touch()
foto2.touch()

shutil.copytree(imagens, backup)