#!/usr/bin/env python3

# numbers = [1, 2, 3, 4, 5, 6] # Se tiver muitos valores, ocupa muito espaço de memória
numbers = range(1, 11) # start, next, stop
print(numbers[-1])
print(numbers[:2])
print("-" * 30)

# Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue
        
    print(f"mais código com {number}")

print("-" * 30)

dados = {}
for line in open("comentarios.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()
print(dados)

print("-" * 30)

original = [1, 2, 3]
# For loops / Laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List Comprehension
dobradaFuncional = [n * 2 for n in original]
print(dobradaFuncional)

# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip() 
    for line in open("comentarios.txt") 
    if ":" in line
}
print(dados)
