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
from utilitarios.utils_bees import(
    capturar_token_bees
)


def bees_deliver(metadado, usuario, senha, formato):
    print("metadado de interface bees deliver")
    match metadado["periodo"]:
        case "diario":
            datas = metadado["datas"]
            relatorio_diario( usuario, senha, formato, metadado, datas )




def relatorio_diario(usuario, senha, formato, metadado, datas):
    
    capturar_token_bees()



    
    