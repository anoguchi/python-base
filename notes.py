#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tecnologia
text: 
Anotação geral sobre tecnologia.

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

comandos = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print("you must specify subcommand {cmds}")
    sys.exit(1)


if arguments[0] not in comandos:
    print("Invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag == arguments[1].lower():
            print("-" * 30)
            print()
            print(f"titulo: {titulo}")
            print(f"texto: {texto}")
            print("-" * 30)
    

if arguments[0] == "new":
    # criação da nota
    titulo = arguments[1] # TODO: Tratar exception
    texto = [
        f"{titulo}",
        input("tag:").strip(),
        input("texto:\n").strip(),
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(texto) + "\n")













    
