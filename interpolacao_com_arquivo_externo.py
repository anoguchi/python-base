#!/usr/bin/env python

"""email span
"""
__version__ = "0.1.0"
__author__ = "Alberto"

import sys            
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informar o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, templatename) #email_tmpl.txt


for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "problemas de escrita.",
            "link": "https://canetalegal.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)
