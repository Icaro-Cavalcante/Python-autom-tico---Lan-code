# Exercício 1 – Cadastro simples
# Crie um arquivo chamado cadastro.xlsx com uma aba chamada Pessoas.
# Adicione os seguintes dados nas células manualmente (com planilha["A1"] = ...):

# | Nome     | Cidade         |
# |----------|----------------|
# | João     | Recife         |
# | Marina   | São Paulo      |
# | Otávio   | Belo Horizonte |
# E salve o arquivo

from openpyxl import Workbook
arquivo = Workbook()

pessoas = arquivo.active
pessoas.title = "Pessoas"

pessoas["A1"] = "Nome"
pessoas["B1"] = "Cidade"

pessoas["A2"] = "--------"
pessoas["B2"] = "---------------"

pessoas["A3"] = "João"
pessoas["B3"] = "Recife"

pessoas["A4"] = "Mariana"
pessoas["B4"] = "São Paulo"

pessoas["A5"] = "Otávio"
pessoas["B5"] = "Belo Horizonte"

arquivo.save(r"15 - Openpyxl\01 - Inserção de dados\exercicios\exercicios\cadastro.xlsx")