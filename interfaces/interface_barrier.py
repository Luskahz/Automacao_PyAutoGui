from interfaces.promax import promax
from interfaces.bees_deliver import bees_deliver
from logins.login_promax import login_promax
import pyautogui
from dotenv import load_dotenv
import os


load_dotenv()


def identificar_interface(metadado, formato) -> str | None:
    if not metadado:
        return None
    
    print("Validação da base, base que está sendo atualizada: " + metadado["rotina"])


    match formato:
        case "especifico":
            match metadado["interface"]:
                case "promax":
                    usuario_promax = os.getenv("usuario_promax")
                    senha_promax = os.getenv("senha_promax")
                    promax(metadado, usuario_promax, senha_promax, formato)
                case "bees_deliver":
                    #implementar puxar usuario e senha do bees
                    bees_deliver()

        case "automatico":
            match metadado["interface"]:
                case "promax":
                    usuario_promax = os.getenv("usuario_promax")
                    senha_promax = os.getenv("senha_promax")
                    login_promax(usuario_promax, senha_promax)
                    promax(metadado, usuario_promax, senha_promax, formato)
    
