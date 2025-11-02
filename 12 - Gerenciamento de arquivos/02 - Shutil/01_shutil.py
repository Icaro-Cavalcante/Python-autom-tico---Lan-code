import shutil
from pathlib import Path

arquivo = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\arquivo.txt")

arquivo.touch(exist_ok=True)

shutil.copy(r"12 - Gerenciamento de arquivos\02 - Shutil\mensagem.txt", r"12 - Gerenciamento de arquivos\02 - Shutil\backup\mensagem_backup.txt" \
"")

shutil.copytree(r"12 - Gerenciamento de arquivos\02 - Shutil\backup", r"12 - Gerenciamento de arquivos\02 - Shutil\pasta 2", dirs_exist_ok=True)

shutil.move(arquivo, r"12 - Gerenciamento de arquivos\02 - Shutil\pasta 2\arquivo2.txt")

pasta3 = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\pasta 3")

shutil.copytree(r"12 - Gerenciamento de arquivos\02 - Shutil\backup", pasta3, dirs_exist_ok=True)

pause = input("")

# shutil.rmtree(pasta3)

mensagem = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\mensagem.txt")

shutil.make_archive(pasta3, "zip", r"12 - Gerenciamento de arquivos\02 - Shutil\pasta 3")

shutil.unpack_archive(r"12 - Gerenciamento de arquivos\02 - Shutil\pasta 3.zip", r"12 - Gerenciamento de arquivos\02 - Shutil\pasta 4")