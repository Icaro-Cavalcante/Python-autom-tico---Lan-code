# Exercício 1 – Contagem regressiva para o fim do ano
# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

from datetime import datetime, timedelta

hoje = datetime.now()
fim_ano = datetime(hoje.year, 12, 31)
contagem = fim_ano - hoje
contagem = contagem.days
print(f"Faltam {contagem + 1} dias.")