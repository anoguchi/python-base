#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento

[operacao] [numero01] [numero02]

Operacões:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py 
operação: sum
numero01: 5
numero02 : 4
9
"""

__version__ = "0.1.0"
__author__ = "Alberto"


import sys


while True:
    arguments = sys.argv[1:]    
    # Validação
    if not arguments:
        operation = input("operação:")
        numero01 = input("numero01:")
        numero02 = input("numero02:")
        arguments = [operation, numero01, numero02]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")

    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    print(nums)
    validated_nums = []
    for num in nums:
    # TODO: Repetição com while + Exceptions
        if not num.replace(".","").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)
    print(validated_nums)

    # Desempacota para ficar mais fácil de utilizar
    numero01, numero02 = validated_nums

    # TODO: Usar dicionário de funções
    if operation == "sum":
        result = numero01 + numero02
    elif operation == "sub":
        result = numero01 - numero02
    elif operation == "mul":
        result = numero01 * numero02
    elif operation == "div":
        result = numero01 / numero02

    print(f"O resultado é {result}")

    continuar = input(f"Quer fazer nova operação? [N/y]").strip().lower()
    if continuar != "y":
        break
        
