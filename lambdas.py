#!/usr/bin/env python3

def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


# Nossa função principal:
def faz_algo(valor, funcao):
    print(f"Aplicando a {funcao} em {valor}")
    return funcao(valor)


names = ["Alberto", "Julia", "Joao", "Ivete", "Zé"]

print(sorted(names, key=lambda name: name.count("e")))


print(list(filter(lambda name: name[0].lower() == "j", names)))

print(list(map(lambda name: "Hello " + name, names)))


# Calculadora
operacao = input("Operacao: [sum, mul, div. sub]:")
n1 = input("n1: ").strip()
n2 = input("n2: ").strip()

def soma(a, b):
    return a + b

operacoes = {
    "sum": soma,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}
resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é: {resultado}")
