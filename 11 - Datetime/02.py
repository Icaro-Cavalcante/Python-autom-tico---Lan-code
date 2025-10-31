from datetime import datetime, timedelta

hoje = datetime.now()
um_dia = timedelta(days=1)

amanha = hoje + um_dia
ontem = hoje - um_dia
print(f"Hoje: {hoje}\nAmanhã: {amanha}\nOntem: {ontem}")

prazo = datetime(2025, 11, 15)

if hoje > prazo:
    print("Prazo estourado.")
else:
    print("no prazo.")

new = datetime(2026, 1, 1)
ano_novo = new - hoje
ano_novo = ano_novo.days
print(f"{ano_novo} dias até o ano novo.")