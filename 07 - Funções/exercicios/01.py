# Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.

# Depois, use a função com um valor recebido via input() e exiba o resultado com print().

def quadrado(numero):
    return numero ** 2
resultado = quadrado(int(input("Digite um número: ")))
print(f"O quadrado desse número é: {resultado}")