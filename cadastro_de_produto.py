#!/usr/bin/env pyhton3
"""Cadastro de produto"""
__version__= "0.1.0"

# produto_nome = "Caneta"
# produto_cor1 = "azul"
# produto_cor2 = "branco"
# produto_preco = 3.23
# produto_dimensao_altura = 12.1
# produto_dimensao_largura = 0.8
# produto_em_estoque = True
# produto_codigo = 45678
# produto_codebar = None

produto = {
    "nome": "Caneta",
    "cores": ["azul","branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Bruno"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} de {compra['produto']['nome']} "
    f" e pagou o total de {total_compra}")

