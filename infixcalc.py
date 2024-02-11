#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1:5
n2:4
9

Os resultados serão salvos em 'infixcalc.log'
"""

__version__ = "0.1.0"

from logging import exception
import os
import sys
from datetime import datetime

while True:

    args = [f for f in sys.argv[1:]]
    number_args = len(args)
    operations = {"sum":"add","sub":"sub","mul":"mul","div":"truediv"}
    keys_operations = list(operations.keys())

    path = os.curdir
    filepath = os.path.join(path, "infixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER','anonymous')

    ## Verifica se não foi passado nenhum argumento e pede input do usuário
    if number_args == 0:
        operation = input("operação: ")
        n1 = float(input("n1: "))
        n2 = float(input("n2: "))
    elif number_args == 3:
        operation = args[0] 
        n1 = float(args[1])
        n2 = float(args[2])
    else:
        sys.exit(f"É necessário que sejam informados 3 argumentos, sendo um operador e 2 números.\n Foram informados {number_args} argumento(s)")

    ## Realiza a operação se forem passados os argumentos corretos.   
    if operation in operations:
        attr = f"__{operations[operation]}__"
        result = getattr(n1,attr)(n2)
        print(f"{result}")
        try:
            with open(filepath, "a") as file_:
                file_.write(f"{timestamp} - {user} -{operation},{n1},{n2} = {result}\n")
        except PermissionError as e:
            # TODO: logging
            print(str(e))
            sys.exit(1)
    else:
        print(f"""São aceitos apenas uma das 4 operações a seguir: {keys_operations}""")

    if input("Pressione enter para continuar ou qualquer tecla para sair")
        break