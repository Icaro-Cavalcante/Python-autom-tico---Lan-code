# Exercício 3 – Detectando palavras proibidas
# Peça ao usuário para escrever uma mensagem.
# Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

mensagem = str(input("Digite uma mensagem: "))
if "bomba" in mensagem.lower():
    print("Alerta! Palavra proibida.")
else:
    print("ok")