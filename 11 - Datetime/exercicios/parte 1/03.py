# Exercício 3 – Assinatura digital do terminal
# Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:

# Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02
# A data e horário devem ser do momento atual da assinatura

from datetime import datetime

def assinatura(nome):
    acesso = datetime.now()
    print(f"Assinatura gerada por {nome} em {acesso.day} do mês {acesso.month} de {acesso.year} às {acesso.hour}:{acesso.minute}")
    
assinatura("Icaro")