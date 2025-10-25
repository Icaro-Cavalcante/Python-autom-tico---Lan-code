# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

soma = 0

for i in range (1, 5 + 1):
    num = float(input(f"Digite o número {i}: "))
    soma+= num
print(f"Soma = {soma}")