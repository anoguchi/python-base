#!/usr/bin/env python3

"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Beto",
    "Julia", 
    "Bruno", 
    "Barbara", 
    "Bia",
]

# Estilo funcional
print("Estilo funcional:")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print("-" * 30)

#Estilo procedural
print("Estilo procedural:")

def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == "b"
    # return text.startswith(("b", "B"))

filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)

# List aplica uma função em todos os elementos da minha lista
# print(*list(filter(starts_with_b, names)), sep="\n")
