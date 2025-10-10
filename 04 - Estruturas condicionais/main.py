# if - Caso a condição seja atendida o código é executado
# elif - Senão, se essa condição for verdade esse código é executado
# else - Senão, esse código é executado

#idade = int(input("Qual sua idade? "))
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

linguagem = "java"
if linguagem == "python":
    print("Você está programando em python")
elif linguagem == "java":
    print("Você está programando em java")
else:
    print("Você está programando em outra linguagem")

senha = "senha123"
if senha != "senha123":
    print("Senha incorreta.")
else:
    print("Senha correta.")

print(senha == "senha123") # Aqui é retornado um boolean, que mostra se a condição é verdadeira ou falsa