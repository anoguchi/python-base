#!/usr/bin/env python3

nome = "Global"

def funcao():
    nome = "Local"
    print("Nome local: ", nome)
    nome = globals()["nome"]
    print("Nome global :", nome)

funcao()
