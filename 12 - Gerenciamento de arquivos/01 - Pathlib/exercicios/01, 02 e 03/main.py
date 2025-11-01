# Exercício 1 – Criando estrutura de pastas
# Crie a seguinte estrutura:

# ├──dados/
# │  ├── entrada/
# │  └── saida/
# ├──relatorios/
# Crie todas as pastas em uma única execução do seu código.

from pathlib import Path
relatorios = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\exercicios\01, 02 e 03\relatorios")
relatorios.mkdir(exist_ok=True, parents=True)
entrada = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\exercicios\01, 02 e 03\dados\entrada")
entrada.mkdir(exist_ok=True, parents=True)
dados = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\exercicios\01, 02 e 03\dados\saida")
dados.mkdir(exist_ok=True, parents=True)

# Exercício 2 – Criar vários arquivos de exemplo
# Dentro da pasta entrada/, crie 3 arquivos vazios:

# dados1.txt
# dados2.txt
# dados3.txt

dados1 = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\exercicios\01, 02 e 03\dados\entrada\dados1.txt")
dados2 = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\exercicios\01, 02 e 03\dados\entrada\dados2.txt")
dados3 = Path(r"12 - Gerenciamento de arquivos\01 - Pathlib\exercicios\01, 02 e 03\dados\entrada\dados3.txt")


dados1.touch()
dados2.touch()
dados3.touch()

# Exercício 3 – Conferindo e filtrando arquivos .txt
# Liste todos os arquivos .txt dentro de entrada/.

# Imprima apenas o nome do arquivo (sem o caminho completo).

for file in entrada.glob("*.txt"):
    print(file.name)