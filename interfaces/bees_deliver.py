import pyautogui
from datetime import datetime
from logins.login_promax import login_promax
import time 
import pyperclip
import subprocess
import re
import pygetwindow as gw
import pyautogui
import os

import os
import time
import subprocess
from playwright.sync_api import sync_playwright
import json
from datetime import datetime, timedelta
import requests

from utilitarios.utils_bees import(
    capturar_token_bees,
    token_bees_valido
)
from utilitarios.utils_global import(
    movimentacao_arquivo_sql,
    MESES
)

def bees_deliver(metadado, usuario, senha, formato):
    print("metadado de interface bees deliver")
    match metadado["periodo"]:
        case "diario":
            datas = metadado["datas"]
            relatorio_diario( usuario, senha, formato, metadado, datas)




def relatorio_diario(usuario, senha, formato, metadado, datas):
    agora = datetime.now()
    if token_bees_valido() is not True:
        print("iniciando apuração do token")
        capturar_token_bees()
    print("token ainda valido! realizando as requisições")

    with open("tokens/bees.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        print(dados)

    headers = dados["request_headers"]
    request_line = dados["request_line"]
    url_base = request_line.split(" ")[1]


    diretorioSqlDir = rf"S:\Logistica\0.DPO\Diretórios_SQL\{metadado['caminho_sql']}\{agora.year}\{MESES[agora.month]}"
    for chave, data in datas.items():
        print(f"Requisitando data {chave}: {data}")

        import urllib.parse as urlparse
        from urllib.parse import parse_qs

        parsed = urlparse.urlparse(url_base)
        print(parsed)
        qs = parse_qs(parsed.query)
        print(qs)
        # substitui APENAS a data
        qs["date"] = [data]
        print(qs)

        nova_query = urlparse.urlencode(qs, doseq=True)
        nova_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{nova_query}"

        print("URL:", nova_url)

        # requisitando
        resp = requests.get(nova_url, headers=headers)

        if resp.status_code != 200:
            print("Erro ao baixar:", resp.status_code)
            continue

        nome = f"bees_deliver_{data}.csv"

        with open(nome, "wb") as f:
            f.write(resp.content)

        print("Arquivo salvo:", nome)
        movimentacao_arquivo_sql(nome, )
    
        #mandar o arquivo pro sql:
        





    
    