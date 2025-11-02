# 2. Mover e renomear arquivos automaticamente
# Crie um script que:

# Verifica se existe um arquivo chamado relatorio.txt.

# Move esse arquivo para uma pasta chamada relatorios_antigos.

# Durante a movimentação, renomeie o arquivo para relatorio_backup.txt.

from pathlib import Path
import shutil

relatorio = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\02\relatorio.txt")
relatorios_antigos = Path(r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\02\relatorios_antigos")
relatorio.touch()

if relatorio.exists:
    relatorios_antigos.mkdir(exist_ok=True)
    shutil.move(relatorio, r"12 - Gerenciamento de arquivos\02 - Shutil\exercicios\02\relatorios_antigos\relatorio_backup.txt.")