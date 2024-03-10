#!/usr/bin/env python3
"""Hello world com dicionario
"""
___version__ = "0.1.0"
__author__ = "Alberto"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo!",
    "C.UTF": "Holá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
