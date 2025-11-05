# 📁 Projeto: Organizador de Arquivos por Extensão
# 🎯 Objetivo
# Criar um programa em Python capaz de organizar automaticamente os arquivos de uma pasta, movendo-os para subpastas com base em suas extensões (como .pdf, .png, .txt, etc.). O programa também deve registrar cada movimentação feita em um arquivo de log.

# 📌 Requisitos
# Seu programa deve:

# Percorrer todos os arquivos de uma pasta chamada organizador. (Arquivo anexado)

# Identificar a extensão de cada arquivo (exemplo: .pdf, .jpg, .py, etc.).

# Criar subpastas com os nomes das extensões (caso ainda não existam).

# Mover os arquivos para as subpastas correspondentes.

# Registrar todas as ações feitas em um arquivo registro.log, com data, hora, nome do arquivo e destino final.

# Ao final da execução, exibir no terminal um resumo com:

# Quantos arquivos foram organizados

# Quais extensões foram encontradas

from datetime import datetime
from pathlib import Path
import shutil

contador_arquivos = 0
contador_extensoes = []

shutil.unpack_archive(r"13 - Projeto Organizador de arquivos\organizador.zip", r"13 - Projeto Organizador de arquivos\organizador")
organizador = Path(r"13 - Projeto Organizador de arquivos\organizador")
pasta_projeto = Path(r"13 - Projeto Organizador de arquivos")
log = Path(pasta_projeto/"resgistro.log")
log.touch()


for file in organizador.iterdir():
    contador_arquivos += 1
    agora = datetime.now()
    agora = agora.strftime("dia %d de %h de %Y, às %H:%M.")
    sufixo = file.suffix
    if sufixo not in contador_extensoes:
        contador_extensoes.append(sufixo)
    nome = file.name
    caminho = (organizador/nome)
    pasta = (pasta_projeto/sufixo)
    pasta.mkdir(exist_ok=True)
    with open (log, mode='a', encoding='utf-8') as arquivo:
        escrita = (f"{agora}. Arquivo {nome} movido para {pasta}.\n")
        arquivo.write(escrita)
    shutil.move(caminho, pasta)

print(f"Foram organizados {contador_arquivos} arquivos.\nForam encontradas as extensões {contador_extensoes}")
organizador.rmdir()