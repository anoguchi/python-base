#!/usr/bin/env python3

# Set, dict, list

s = set()
s.add(1)

d = {}
d["key"] = "value"

l = []
l.append(0)

# Vai adicionar na mesma lista(isso é perigoso) - melhor para cache
def adicionar_a_lista(valor, lista=[]):
    lista.append(valor)
    return lista

adicionar_a_lista(4)
adicionar_a_lista(5)
print(adicionar_a_lista(6))



# Vai criar uma nova lista
def adicionar_a_lista02(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista

adicionar_a_lista02(4)
adicionar_a_lista02(5)
print(adicionar_a_lista02(6))
