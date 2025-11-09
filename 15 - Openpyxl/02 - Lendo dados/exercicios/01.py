# Exercício 1 – Dados pontuais
# Abra a aba Alunos e imprima os valores exatos das seguintes células:

# B2
# D5
# E10

from openpyxl import load_workbook

arquivo = load_workbook(r"15 - Openpyxl\02 - Lendo dados\exercicios\alunos.xlsx")
alunos = arquivo['Alunos']

print(alunos["B2"].value)
print(alunos["D5"].value)
print(alunos["E10"].value)