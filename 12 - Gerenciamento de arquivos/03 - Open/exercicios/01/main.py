# Exercício 1 — Criando um relatório simples
# Crie um arquivo chamado relatorio.txt que contenha a frase "Estou aprendendo Python!

# Inclua no final do arquivo a data e hora de criação do arquivo de forma automática

from datetime import datetime
agora = datetime.now()
agora = agora.strftime("Dia %d de %h de %Y, às %H:%M.")

relatorio = r"12 - Gerenciamento de arquivos\03 - Open\exercicios\01\relatorio.txt"

with open(relatorio, mode='w+', encoding="utf-8") as file:
    file.write(f"Estou aprendendo Python!\n{agora}")
    file.seek(0)
    print(file.read())


