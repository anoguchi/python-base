#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

----Tabuada do 1----

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
##########
----Tabuada do 2----

    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
...
##########
"""
__version__ = "0.1.1"
__author__ = "Alberto"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = range(1, 11)

# para cada numero em numeros
for numero01 in numeros:
    # "{:-^19}" = centralizar e colocar o caracter "-" x vezes
    print("{:-^19}".format(f"Tabuada do {numero01:02d}"))
    print()
    for numero02 in numeros:
        resultado = numero01 * numero02
        print("{:^18}".format(f"{numero01} x {numero02} = {resultado}"))
    print()
    print("#" * 19)
    print()



