# Exercício 3 – Validade de produto 🥫
# Peça ao usuário para informar a data de fabricação de um produto.
# Considere que ele vence em 180 dias.
# Mostre:

# A data de validade

# Se o produto ainda está válido ou já venceu

# Quantos dias faltam ou há quanto tempo passou do prazo

from datetime import datetime, timedelta

atual = datetime.now()
produto = str(input("Digite a data de fabricação do produto (d/m/a): "))
produto = datetime.strptime(produto,"%d/%m/%Y")
validade = timedelta(days=180)
validade = produto + validade

print(validade, atual)

if atual < validade:
    print("O produto está na validade.")
    print(f"Faltam {(validade - atual).days + 1} dias.")
elif validade < atual:
    print("O produto está fora da validade.")
    print(f"Se passaram {(atual - validade).days + 1} dias.")