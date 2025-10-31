from datetime import datetime
agora = (datetime.now()) # Agora

# print(agora, "\n")
# print(agora.day) # dia
# print(agora.month) # mes
# print(agora.year) # ano
# print(agora.hour) # hour
# print(agora.minute) # minuto
# print(agora.second) # segundo

aniversario = datetime(2006,10,30)
print(aniversario)

print(agora.strftime("Hoje é dia %d, do mês %m, do ano %Y.")) # Transforma em string

data_str = "20/04/2025"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
print(data_convertida)