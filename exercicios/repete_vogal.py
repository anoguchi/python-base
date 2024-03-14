#!/usr/bin/env python3

"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprima
cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogal.py
"Digite uma palavra (ou enter para sair): " Python
"Digite uma palavra (ou enter para sair): " Beto
"Digite uma palavra (ou enter para sair): " <enter>
Pythoon
Beetoo
"""

import sys
import re
import logging
log = logging.Logger("Alerta")

words = []
while True:
    word = input("Digite um palavra (ou enter para sair): ").strip()
    if not word: # Condição de parada
        break
        
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiouãáàéèíìõóòúù":
            final_word += letter * 2
        else:
            final_word += letter

    # Usando ternário
    '''
    final_word += (
        letter * 2
        if letter.lower() in "aeiouãáàéèíìõóòúù" 
        else letter
    )
    '''
    words.append(final_word)

print(*words, sep="\n") # Desempacota o que tiver em words
    




   

