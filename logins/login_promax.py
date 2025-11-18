import time
import subprocess
import pygetwindow as gw
import mss

import pyautogui
from PIL import Image
import pytesseract
from unidecode import unidecode
from utilitarios.utils_promax import(
    write_lower,
    janela_contem_texto
)


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\lucas.l\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

URL_PROMAX = "https://imarui.promaxcloud.com.br/pw/"

def validar_tela_login(timeout=60, intervalo=1):
    """
    Abre o Edge, espera até que a tela de login apareça (detecta por OCR).
    Retorna True assim que encontrar, ou False se expirar o timeout.
    """
    subprocess.Popen(["start", "msedge", URL_PROMAX], shell=True)
    print("🌐 Abrindo Edge...")
    while janela_contem_texto("Login de Usuario", "PromaxWeb") is not True:
        print("aguardando abrir a janela do edge")
    print("janela do edge aberta")

    wins = [w for w in gw.getWindowsWithTitle("Edge") if w.visible]

    if not wins:
        raise RuntimeError("❌ Nenhuma janela do Edge encontrada.")
    win = wins[0]

    if win.isMinimized:
        win.restore()
    win.activate()
    win.maximize()
    time.sleep(1)

    print("🔍 Aguardando aparecer 'Login de Usuário' na tela...")

    inicio = time.time()
    with mss.mss() as sct:
        while time.time() - inicio < timeout:

            bbox = {"top": win.top, "left": win.left, "width": win.width, "height": win.height}
            sct_img = sct.grab(bbox)
            img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)

            texto = pytesseract.image_to_string(img, lang="eng")
            texto_normalizado = unidecode(texto.lower())

            if "login de usuario" in texto_normalizado:
                print("✅ Tela de login detectada!")
                return True

            time.sleep(intervalo)

    print("⛔ Timeout: Tela de login não apareceu.")
    return False

def login_promax(usuario, senha):
    inicio = time.time()
    timeout = 60  
    while not validar_tela_login():
        if time.time() - inicio > timeout:
            raise TimeoutError("⛔ Tela de login não detectada em 60s.")
        time.sleep(1)

    write_lower(usuario)
    pyautogui.press('tab')
    pyautogui.press(senha)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    for _ in range(5):
        pyautogui.press("tab")