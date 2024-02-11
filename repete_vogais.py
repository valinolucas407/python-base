#!/usr/bin/envpython3
"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

python repete_vogal.py
'Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>

"""

import sys

count = 0
word_list = []
vogais = ['a','e','i','o','u','A','E','I','O','U']

word  = input("Digite uma palavra (ou enter para sair):").strip()

while word:
    letter_list = list(word)
    index_ = []
    for i, letter in enumerate(letter_list):
        if letter in vogais:
            letter_list[i] = letter_list[i] * 2
        else:
            continue
    word_list.append(''.join(letter_list))
    word  = input("Digite uma palavra (ou enter para sair):").strip()

print(*word_list, sep="\n")