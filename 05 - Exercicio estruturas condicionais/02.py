# Verificação de Diferença:
# Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.".

nome1 = str(input("Digite o nome 1: "))
nome2 = str(input("Digite o nome 2: "))
if nome1 != nome2:
    print(f"Os nomes são diferentes.")
else:
    print(f"Os nomes são iguaisi.")