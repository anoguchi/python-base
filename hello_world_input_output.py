#!/usr/bin/env python3
"""Hello world Mult Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar: 

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe a através do CLI argument `--lang`

Ou o usuário terá que digitar

Execução:

    python3 hello_world_input_output.py
    ou
    ./hello_world_input_output.py

"""
___version__ = "0.1.0"
__author__ = "Alberto"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else: 
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo!",
    "C.UTF": "Holá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}
print(msg[current_language] * int(arguments["count"]))

