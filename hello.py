#! /usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurando no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_br

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.1.2"
__author__ = "Lucas Valino"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
