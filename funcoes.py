#!/usr/bin/env python3
"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""
import math
from math import sqrt

# SOLID - Single Responsibility

def f(x): # Assinatura
    return 5 * (x / 2)

def double(x):
    return x * 2

valor = double(f(10))
print(valor)
print(f(10))
print(f(10) == 25)


###
"""
Essa função não retorna nada. Se tentarmos guardar ela em um 
variável o valor será None. Quando ela não retorna nada, não faz sentido 
guardarmos o resultado dela. Funções que não retornam nada são chamadas
de Procedimentos / Procedures
"""
def print_in_upper(text):
    print(text.upper())

print_in_upper("Beto")

###
# Calcula a area de um triangulo sabendo apenas as medidas dos lados
def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5

# Muito comum uma função dar apoio a outra.
def heron2(params):
    return heron(*params)

area_triangulo = heron(3, 4, 5)
print(area_triangulo)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (3, 4, 5),
    (30, 44, 55),
    (32, 33, 35)
]

for t in triangulos:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")

for t2 in triangulos:
    area = heron2(t)
    print(f"A area do triangulo é: {area}")

print(list(map(heron2, triangulos)))

###
def nome_da_funcao():
    print("Hello funcao")
    return 1

result = nome_da_funcao();
print(result)
