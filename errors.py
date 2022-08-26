#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to Ask Forgiveness than permission

try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)