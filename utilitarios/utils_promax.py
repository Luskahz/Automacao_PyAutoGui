import time
import pyautogui
import pygetwindow as gw
import os
from datetime import datetime
import os
import shutil
import keyboard 
import pytesseract
import pygetwindow as gw
import mss
from PIL import Image
from unidecode import unidecode


EXT = "csv"
DOWNLOADS_DIR = os.path.expanduser(r"~\Downloads")
MESES = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }


def write_lower(texto: str):
    if keyboard.is_pressed('caps lock'):
        pyautogui.press('capslock')
    pyautogui.write(texto.lower())

def match_progresso(texto):
    texto = texto.replace(" ", "")
    if "% de" not in texto:
        return False
    
    parte_num = texto.split("% de")[0]

    if not parte_num.isdigit():
        return False

    num = int(parte_num)
    return 1 <= num <= 100


def exportar_csv(janela):
    for _ in range(13):
        pyautogui.press('tab')
    pyautogui.press('enter')
    while janela_contem_texto("processando", janela) is True:
        print("carregando arquivo para download")
    while janela_contem_texto(["Deseja abrir ou salvar", "Abrir"], janela) is not True:
        print("Aguardando download da base")
    time.sleep(1)
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')
    texto_concluido= [ "concluído.", "concluido", "concludo", "Abrir", "conclude"]
    texto_pendente = [match_progresso, "baixados", "s restantes"]
    time.sleep(2)
    while janela_contem_texto(texto_concluido, janela) is not True and janela_contem_texto(texto_pendente, janela) is True:
        print("Aguardando download da base")
    for _ in range(19):
        pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

def renomear_arquivo(novo_nome):
    pyautogui.press('f2')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.15)
    write_lower(novo_nome)
    pyautogui.press('enter')
    pyautogui.press('enter')

def fechar_janelas(janelas_relatorio):
    time.sleep(1)

    # --- Correção aqui ---
    # Se vier uma string única, transforma em lista com 1 elemento
    if isinstance(janelas_relatorio, str):
        alvos = [janelas_relatorio]
    else:
        alvos = janelas_relatorio
    # ----------------------

    for titulo in alvos:
        janelas = gw.getWindowsWithTitle(titulo)
        if not janelas:
            print(f"🔍 Nenhuma janela encontrada com título: {titulo}")
            continue

        for janela in janelas:
            if janela.visible:
                try:
                    if janela.isMinimized:
                        janela.restore()
                    janela.activate()
                    janela.close()
                    print(f"✅ Fechou janela: {janela.title}")
                    time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Erro ao fechar {janela.title}: {e}")

    print("🎯 Fechamento concluído.")


def focar_janela(nome_janela: str):
    """
    Ativa (coloca na frente) a janela cujo título contenha 'nome_janela'.
    """

    time.sleep(0.5)

    janelas = gw.getWindowsWithTitle(nome_janela)

    if not janelas:
        print(f"🔍 Nenhuma janela encontrada contendo: {nome_janela}")
        return False

    # pega a primeira janela compatível
    janela = janelas[0]

    try:
        if janela.isMinimized:
            janela.restore()

        janela.activate()
        print(f"🔝 Ativada: {janela.title}")
        return True

    except Exception as e:
        print(f"⚠️ Erro ao ativar {janela.title}: {e}")
        return False

def acessar_rotina(rotina):
    write_lower(rotina)
    pyautogui.press('tab')
    pyautogui.press('enter')

def encontrar_arquivo_exportado(downloads_dir, prefixo):
    arquivos = []

    for nome in os.listdir(downloads_dir):
        if nome.startswith(prefixo):
            caminho = os.path.join(downloads_dir, nome)
            modificado = os.path.getmtime(caminho)
            arquivos.append((modificado, caminho))

    if not arquivos:
        return None 
   
    arquivos.sort(reverse=True)

   
    return arquivos[0][1]



def movimentacao_arquivo_sql(nome_pos_promax, agora: datetime, metadado):
    if "datas" not in metadado: 
        print("mensal")
        diretorioSqlDir = rf"S:\Logistica\0.DPO\Diretórios_SQL\{metadado['caminho_sql']}\{agora.year}"
        destino = os.path.join(diretorioSqlDir, f"{MESES[agora.month]}.{EXT}")
        original = os.path.join(DOWNLOADS_DIR, nome_pos_promax)
    else:
        diretorioSqlDir = rf"S:\Logistica\0.DPO\Diretórios_SQL\{metadado['caminho_sql']}\{agora.year}\{MESES[agora.month]}"
        dia = datetime.strptime(metadado["datas"]["d1"], "%d/%m/%Y").day
        prefixo = f"{metadado['nome_exportacao']}{dia}"
        print(f"🔎 Aguardando arquivo iniciar download (prefixo: {prefixo})")
        arquivo_encontrado = None
        inicio = time.time()
        timeout = 30

        while arquivo_encontrado is None:
            arquivo_encontrado = encontrar_arquivo_exportado(DOWNLOADS_DIR, prefixo)

            if arquivo_encontrado:
                print("📥 Arquivo detectado:", arquivo_encontrado)
                break

            if time.time() - inicio > timeout:
                print(f"⚠️ Timeout: nenhum arquivo encontrado com prefixo {prefixo}")
                return

            time.sleep(1)

        destino = os.path.join(diretorioSqlDir, f"{dia}.{EXT}")
        original = arquivo_encontrado
        print("diaria")

    print(nome_pos_promax)
    print(diretorioSqlDir)
    print(destino)
    print(f"🔎 Procurando arquivo: {original}")
    print("chegou aqui, esperando 10s")
    inicio_espera = time.time()
    
    while not os.path.exists(original): #espera 30 segundos o arquivo ser salvo no downloads, se n for ele breka
        if time.time() - inicio_espera > 30:
            print("⚠️ Timeout: arquivo ainda não apareceu no diretório de downloads.")
            break
        time.sleep(1)

    if not os.path.exists(original):
        print(f"❌ Arquivo {nome_pos_promax} não encontrado no Downloads.")
    else:
        os.makedirs(diretorioSqlDir, exist_ok=True)
        if os.path.exists(destino):
            os.remove(destino)
            print(f"⚠️ Substituído arquivo existente: {destino}")

        shutil.move(original, destino)
        print(f"✅ Arquivo movido com sucesso para: {destino}")


def inserir_datas(data_inicio_m0, data_fim_m0):
    write_lower(data_inicio_m0)
    pyautogui.press('tab')
    write_lower(data_fim_m0)



def janela_contem_texto(texto_procurado, nome_janela: str) -> bool:
    """
    Verifica se a janela contém um ou mais textos.
    texto_procurado pode ser:
        - string: busca única
        - lista/tupla: tenta cada texto; se um der True, retorna True
    """

    # --- encontrar janela ---
    janelas = gw.getWindowsWithTitle(nome_janela)
    if not janelas:
        return False

    win = janelas[0]

    if win.isMinimized:
        win.restore()

    # --- capturar imagem ---
    with mss.mss() as sct:
        bbox = {
            "top": win.top,
            "left": win.left,
            "width": win.width,
            "height": win.height
        }
        raw = sct.grab(bbox)
        img = Image.frombytes("RGB", raw.size, raw.rgb)

    # --- OCR ---
    texto_ocr = pytesseract.image_to_string(img, lang="eng")
    texto_normalizado = unidecode(texto_ocr.lower())
    

    # --- normalizar entrada ---
    if isinstance(texto_procurado, str):
        textos = [texto_procurado]       
    else:
        textos = list(texto_procurado)    # lista/tupla → lista

    # --- testar um por um ---
    for t in textos:

    # caso seja função (matcher)
        if callable(t):
            if t(texto_normalizado):
                return True
            continue

        # caso seja string (comportamento atual)
        if t.lower() in texto_normalizado:
            return True

    return False

def janela_aberta(nome_janela: str) -> bool:
    nome = nome_janela.lower()
    
    for titulo in gw.getAllTitles():
        if nome in titulo.lower():
            return True

    return False

