#!/usr/bin/env python3

# Escopo global
nome = "Global"
numero = 1
flag = True

def funcao():
    # Escopo local
    nome = "Local"

    def funcao_interna(): # inner function / closure
        # Escopo local da funcao interna
        nome = "Interna"
        print("Escopo local da funcao interna: ", locals())
        print("*" * 30)
        print(nome)
        return nome
        # Termina o escopo da funcao interna
        
    print("Escopo local da funcao: ", locals())
    print("=" * 30)
    funcao_interna()
    print(nome)
    return nome
    # Termina o escopo local

print("Escopo global do programa", globals())
print ("-" * 30)

funcao()
print(nome)

# Termina o escopo global

