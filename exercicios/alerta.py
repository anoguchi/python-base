#!/usr/bin/env python3

"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice da
umidade do ar. Sendo que será exibida uma mensagem de alerta dependendo das 
condições:

temp maior 45: ALERTA! Perigo, calor extremo.
temp vezes 3 for maior ou igual a umidade: ALERTA! Perigo de calor úmido.
temp entre 10 e 30: Normal.
temp entre 0 e 10: Frio.
temp menor que 0: ALERTA! Frio extremo.

"""
import sys
import logging
log = logging.Logger("Alerta")

info = {
    "temperatura": None,
    "umidade": None
}   

# Para não iterar no dict original e sim em uma cópia
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("Alerta! Calor extremo 🥵")
elif temp * 3 >= umidade:
    print("Alerta! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal😁")
elif temp >= 0 and temp <= 10:
    print("Frio🥶")
elif temp < 0: 
    print ("Alerta: Frio extremo ⛄") 
