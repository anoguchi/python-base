#!/usr/bin/env python3
import os
import sys
import time
import logging

log = logging.Logger("errors")
# Com if: LBYL - Look Before You Leap
# Olhe antes de pular/atravessar a rua.

# Com try: EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão

try:
    raise RuntimeError("Subindo um erro")
except Exception as e:
    print(str(e))

print("-" * 30)

# Limite da recursão no python é 1000
def try_to_open_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""   
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    try:
        return open(filepath).readlines() #FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            return try_to_open_file(filepath, retry=retry - 1)
    else:
        print("Sucesso!")
    finally:
        print("Execute isso sempre!")

    return []

for line in try_to_open_file("names.txt", retry=5):
    print(line)


print("-" * 30)
try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
