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
    print(f"you must specify subcommand {comandos}")
    sys.exit(1)


if arguments[0] not in comandos:
    print("Invalid command {arguments[0]}")

while True:

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag? ").strip().lower()
            
        # leitura
        for line in open(filepath):
            titulo, tag, texto = line.split("\t")
            if tag.lower() == arg_tag:
                print("-" * 30)
                print()
                print(f"titulo: {titulo}")
                print(f"texto: {texto}")
                print("-" * 30)
        

    if arguments[0] == "new":
        # criação da nota
        try:
            titulo = arguments[1]
        except IndexError:
            titulo = input("Qual é o titulo? ").strip().title()
        texto = [
            f"{titulo}",
            input("tag: ").strip(),
            input("texto:\n").strip(),
        ]
        # \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(texto) + "\n")

    continuar = input(f"Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
    if continuar != "y":
        break
        












    
