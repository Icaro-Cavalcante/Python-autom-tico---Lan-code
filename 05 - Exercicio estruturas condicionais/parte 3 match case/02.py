# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:

# "carro" → "Veículo terrestre"
# "bicicleta" → "Transporte sustentável"
# "avião" ou "helicóptero" → "Transporte aéreo"

# Qualquer outro → "Transporte desconhecido"

transporte = str(input("Digite um meio de transporte: "))
match transporte:
    case "carro":
        print("Veículo terrestre")
    case "bicicleta":
        print("Transporte sustentável")
    case "aviao" | "helicoptero":
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")