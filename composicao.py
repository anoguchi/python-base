#!/usr/bin/env python3

names = [
    "Beto",
     "Julia", 
     "Bruno", 
     "Barbara", 
     "Bia",
]

# TODO: Usar lambdas
def starts_with_b(text):
    return text[0].lower() == "b"
    # return text.startswith(("b", "B"))

# list aplica uma função em todos os elementos da minha lista
print(*list(filter(starts_with_b, names)))
print(list(filter(starts_with_b, names)))

"""
for name in names:
    if name.lower().startswith("b"):
        print(name)
"""    

