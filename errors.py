#!/usr/bin/env python3
import os
import sys
import time
import logging

log = logging.getLogger("errors")

# EAFP - Easy to Ask Forgiveness than permission

# Resolução com iteração

def try_to_open_a_file(filepath, retry=1) -> list:
    "Tries to open a file, if it error, it retries the operation."
    for atempt in range(1, retry + 1): # o range de (1,1) produz uma lsita vazia, por isso o +1
        try:
            return open(filepath).readlines() # o return faz o break do loop for
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(2)
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []

# Resolução com recursão, o python tem um limite de recursão, 1000 por padrão

# def try_to_open_a_file(filepath, retry=1) -> list:
#     "Tries to open a file, if it error, it retries the operation."
#     try:
#         return open(filepath).readlines()
#     except FileNotFoundError as e:
#         log.error("ERRO: %s", e)
#         time.sleep(2)
#         if retry > 1:
#             return try_to_open_a_file(filepath, retry-1)
    
#     else:
#         print("Sucesso!!!")
#     finally:
#         print("Execute isso sempre!")


for line in try_to_open_a_file("names.txt", 3):
    print(line)
