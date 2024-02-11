#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

SERVER = 'localhost'
PORT = 8025


FROM = "valino_lucas@hotmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este e-mail foi enviado pelo Python.
<b>Olá mundo!</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {" ,".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(SERVER, PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
