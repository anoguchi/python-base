#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam canda
uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala01 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala02 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança",aula_danca)]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print("-" * 50)
    print(f"Alunos da atividade {nome_atividade}:")
    print("")

    atividade_sala01 = []
    atividade_sala02 = []

    for aluno in atividade:
        if aluno in sala01:
            atividade_sala01.append(aluno)
        elif aluno in sala02:
            atividade_sala02.append(aluno)

    print("Sala 01 ", atividade_sala01)
    print("Sala 02 ", atividade_sala02)

