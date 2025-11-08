# Exercício 3 – Multiplas abas e estrutura de planilha
# Crie uma nova aba chamada Visitas.

# Escreva a estrutura da tabela:

# | Data       | Visitantes |
# |------------|------------|
# | 01/01/2025 | 134        |
# | 02/01/2025 | 156        |
# Na aba Visitas, sobrescreva o número de visitantes do dia 01/01/2025 para 142

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

arquivo.create_sheet("Visitas")
visitas = arquivo["Visitas"]

visitas.append(["Data", "Visitantes"])
visitas.append(["------------", "------------"])
visitas.append(["01/01/2025", 134])
visitas.append(["02/01/2025", 156])

visitas["B3"] = "142"

arquivo.save(r"15 - Openpyxl\01 - Inserção de dados\exercicios\exercicios\cadastro.xlsx")