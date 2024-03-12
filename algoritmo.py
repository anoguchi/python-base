#!usr/bin/env python3

"""
Statements 
Se -> if
Senão, se -> elif
Senão -> else
E -> and
OU -> or
Não -> not

Expressions -> bool True, False
é feriado? 
é natal?
é feriado e Não é natal
é sábado?
é sábado OU é domingo?
"""

# Actions (verbos, ação)
# Função / Método / Instrução

# PSEUDO CÓDIGO
import ir, pegar, pedir, tem, comer, ficar

# Premissas
today = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True 
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando): # Começar com o que tem mais condições
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("garrafa-de-agua")
    # Short circuit (se começar o if com if chovendo e ela for true nao irá avaliar as outras)
    elif chovendo:
        pegar("guarda-chuva")
        
    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir(6, "pao integral")
        pedir(6, "baguete")
    elif tem("pao integral") or tem("baguete"):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer pao") 
else:
    ficar("casa")
    comer("bolacha")       
