#! /usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente 
 o programa exibe a mensagem
correspondente.

Como usar: 

Tenha a variavel LANG devidamente configurada ex: 
export LANG=pt_BR

Execucao:
python3 hello.py
ou
./hello.py


"""

__version__ = "0.0.1"
__author__ = "Joao Amaral"
__license__ = "Unlicense"

import os

os.environ["LANG"] = "en_US"  # Simulando a configuração da variável de ambiente LANG

current_language = os.getenv("LANG")[:5]  # Simulando a leitura da variável de ambiente LANG

msg = "Hello, World!!"

if current_language == "pt_br":
    msg = "Olá, Mundo!!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!!"   




print(msg)
