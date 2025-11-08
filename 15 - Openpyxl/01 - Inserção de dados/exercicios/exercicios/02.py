# Exercício 2 – Adicionando dados com append
# No mesmo arquivo cadastro.xlsx, adicione mais duas pessoas na aba Pessoas utilizando o método append():

# Letícia, Porto Alegre

# Gustavo, Salvador

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

pessoas.append(["Letícia", "Porto Alegre"])
pessoas.append(["Gustavo", "Salvador"])

arquivo.save(r"15 - Openpyxl\01 - Inserção de dados\exercicios\exercicios\cadastro.xlsx")