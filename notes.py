#!/usr/bin/env python3

"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid Usage")
    sys.exit(1)

cmds = ("read","new")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    parameters = {}
    notes = {}
    for arg in arguments[1:]:
        key,value = arg.split("=")
        key = key.lstrip("-").strip()
        parameters[key] = value
    with open(filepath) as file_:
        lines = file_.readlines()
        filter_lines = []
        if not parameters:
            print("Nenhum parametro foi passado.")
        else:
            for line in lines:
                if parameters['tag'] in line:
                    filter_lines.append(line)
            for line in filter_lines:
                dict_tags = {}
                tags = line.split(",")[:-1]
                for tag in tags:
                    key, value = tag.split(":")
                    dict_tags[key] = value
                print(dict_tags['text'])
        
if arguments[0] == "new":
    note = {}
    try:
        title = arguments[1]
    except IndexError as e:
        print("[Erro] Ficou faltando informar o título da nota.")
        sys.exit(1)
    tag = input("tag: ")
    text = input("text: ")
    note = f"title:{title},tag:{tag},text:{text}"
    with open(filepath,"a") as file_:
        file_.write(f"{note},\n")

