# Desafio 2 – Criando um pacote de utilidades
# Crie uma pasta chamada meu_pacote

# Dentro dela, crie:

# formatador.py → função caixa_alta(texto) → retorna o texto em letras maiúsculas

# numeros.py → função eh_par(numero) → retorna True se for par

# No main.py:

# Importe e use as funções do pacote

# Exiba o resultado formatado

from meu_pacote.formatador import *
from meu_pacote.numeros import *

print(caixa_alta("icaro"))
print(eh_par(53))