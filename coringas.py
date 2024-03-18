#!/usr/bin/env python3

def soma(a, b):
    return a + b

soma(1, 3)
soma(1, b=3)

def hello(nome, sobrenome="Noguchi"):
    print(f"Hello {nome}, {sobrenome}")

hello("Alberto", "Hideyo")
hello("Julia")
hello(sobrenome="Silva", nome="Diego")
hello("Alberto", sobrenome="Nogushi")

# Coringa, ex: print()
def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)
        
    print(kwargs)
    
    print(f"timeout {timeout}")
    

funcao("Beto", 1, True, [], timeout=90, nome="Beto", data="hoje", teclado=True, panela=3)
