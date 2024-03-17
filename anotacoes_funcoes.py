#!/usr/bin/env python3

"""
A função é formada por alguns elementos:

Atribuição ou definição:
def nome_da_funcao

Assinatura: Tudo dento dos parenteses e até os dois pontos.
(a, b, c):

"""

# Dentro da função podemos colocar outros elementos:
# Documentação ou docstring
def nome_da_funcao(a: int, b: int, c: int) -> int: 
    """Esta função faz algo com a, b e c.
    
    Use esta função quando quiser a + b + c

    >>> nome_da_funcao(1, 2, 3)
    6
    
    Antes do python 3 era feito: 
    
    :param a: Numero inteiro
    :type a: int
    :param b: Numero inteiro
    :type b: int
    :param c: Numero inteiro
    :type c: int
    :return: Retorna o resultado de a + b + c
    :rtype: int
    """
    resultado = a + b + c
    return resultado

# Passagem de argumentos    
valor = nome_da_funcao(1, 2, 3)
print(valor)

"""
Existem algumas formas de passar parametros(valor que esta em aberto) para uma 
função:

Posicional: Forma mais comum quando a função tem poucos argumentos.
(a, b, c)
(1, 2, 3)

Nomeados: Vantagem que conseguimos inverter
(a=1, b=2, c=3)
(b=1, a=2, c=3)

Mista:
(1, c=2, b=3)

# funcao com muitos argumentos
valor = nome_da_funcao(
    1, 
    c=2, 
    b=3,
    d=4,
    e=5, 
    f=6,
)
"""
####################################
"""
valor de retorno: Ela pode retornar mais de um valor de retorno, uma tupla.
A vantagem de usar tuplas, podemos desempacotar diretamente. 
"""
def outra_funcao(a, b, c):
    """Explica o que a funcao faz"""
    return a * 2, b * 2, c *2

outro_valor = outra_funcao(1, 2, 3)
valor1, valor2, valor3 = outra_funcao(1, 2, 3)
print(outro_valor)
print(valor1)
print(valor2)
print(valor3)

valor1, *_ = outra_funcao(1, 2, 3)
print(valor1)

###################################

"""
Passagem de argumentos com desempacotament
"""

def soma(n1, n2):
    """Faz a soma de 2 numeros."""
    return n1 + n2

# Normal
print(soma(10, 20))

# Argumentos em sequencia / posicional
args = (30, 40) # tupla, list, str
print(soma(args[0], args[1]))
print(soma(*args)) # Desempacotar

# Argumentos dicionario / nomeados
args = {"n2": 90, "n1": 100}
print(soma(args["n1"], args["n2"]))
print(soma(n1=args["n1"],n2= args["n2"]))
print(soma(**args)) # Desempacotar

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 30},
    {"n2": 50, "n1": 1000},
    {"n2": 23, "n1": 99},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print("-" * 12)
        print(soma(**item))
    else:
        print("-" * 12)
        print(soma(*item))
