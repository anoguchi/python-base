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

Os resultados serão salvos em `prefixcalc.log`
"""

__version__ = "0.1.0"
__author__ = "Alberto"

import os
import sys
from datetime import datetime

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

validated_nums = []
for num in nums:
# TODO: Repetição com while + exceptions
    if not num.replace(".","").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)

    validated_nums.append(num)

try:
    # Desempacota para ficar mais fácil de utilizar
    numero01, numero02 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1) 


path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

valid_operations = {
    "sum": lambda a, b: a + b, 
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}


result = valid_operations[operation](numero01, numero02)
print(f"O resultado é {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {numero01},{numero02} = {result}\n")
except PermissionError as e:
    print(str(e))
    sys.exit(1)
    
# print(f"{operation}, {numero01},{numero02} = {result}", file=open(filename, "a"))    

    
