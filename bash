import os

os.environ["LANG"] = "es_ES"  # Simulando a configuração da variável de ambiente LANG
current_language= os.getenv("LANG")[:5]  # Simulando a leitura da variável de ambiente LANG

msg = "Hello, World!!"

if current_language == "es_ES":
    msg = "Hola, Mundo!!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!!"

    print(msg)