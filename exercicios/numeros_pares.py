#!/usr/bin/env python3

"""
Faça um programa que imprima os números pares de 1 a 200

ex:
`python numeros_pares.py`

2
4
6
8
...
"""

numbers = range(1, 201)
for number in numbers:
    if number % 2 == 0:
        print(number)
