#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequentam cada uma das atividades
"""

__version__ = "0.1.0"

salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erik", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for atividade in atividades:
    print(f"Alunos da atividade {atividade} \n")
    print("-" *50)

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(salas["sala1"]) & set(atividades[atividade])
    atividade_sala2 = set(salas["sala2"]) & set(atividades[atividade])
    
    print(f"Sala1 ", atividade_sala1)
    print(f"Sala2 ", atividade_sala2)
    print()
    print("#" * 50)
