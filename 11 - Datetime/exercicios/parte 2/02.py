# Exercício 2 – Verificador de evento
# Peça ao usuário que digite uma data de um evento

# Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

from datetime import datetime, timedelta

hoje = datetime.now()

evento = str(input("Digite a data do evento(d/m/a): "))
data = datetime.strptime(evento, "%d/%m/%Y")


if data.day == hoje.day and data.month == hoje.month:
    print("Está acontecendo hoje.")
elif data > hoje:
    restantes = data - hoje
    restantes = restantes.days + 1
    print(f"Ainda restam {restantes} dias.")
else:
    print("O evento já passou.")