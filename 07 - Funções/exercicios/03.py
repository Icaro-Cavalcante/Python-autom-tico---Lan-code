# Crie uma função chamada verificar_par(numero) que retorna:

# "Par" se o número for par
# "Ímpar" se for ímpar

# Peça um número ao usuário com input(), chame a função e mostre o resultado.

num = int(input("Informe o numero: "))
def par_impar(n):
    if n % 2 == 0:
        print(f"O número {n} é par")
    else:
        print(f"O número {n} é ímpar")
par_impar(num)
