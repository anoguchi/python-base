#!/usr/bin/env python3
import os
import sys

# Com if: LBYL - Look Before You Leap
# Olhe antes de pular/atravessar a rua.

# Com try: EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão

try:
    raise RuntimeError("Subindo um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines() #FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry

else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
