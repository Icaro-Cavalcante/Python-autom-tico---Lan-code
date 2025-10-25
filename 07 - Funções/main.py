# Uma função executa um bloco de código

def despedida():
    print("Tchau")

despedida()

# Funções tem parâmetros

def somar(x,y):
    print(f"{x} + {y} = {x+y}")

somar(1,2)

# Funções podem retornar valores

def multiplicacao(x,y):
    return x * y
resultado = multiplicacao(4,5)
print(resultado)