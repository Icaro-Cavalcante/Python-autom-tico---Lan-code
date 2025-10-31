# Exercício 2 – Quantos meses faltam?
# Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

# Hoje é o 4º mês do ano. Ainda faltam 8 meses para terminar o ano!

from datetime import datetime

agora = datetime.now()
data = "20/01/2010"
agora = datetime.strptime(data, "%d/%m/%Y")

print(f"Hoje estamos no mês {agora.month}. Ainda faltam {12 - agora.month} para terminar o ano.")