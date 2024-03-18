#!/usr/bin/env python3
import time

def imprime_nome(nome, sobrenome = "Hideyo"):
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Alberto", "Noguchi")
imprime_nome("Julia", "Noguchi")
imprime_nome("Beto")

def conecta(host, timeout=10):
    print(f"conectando com {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("error ao conectar")

conecta("localhost", 5)
    
