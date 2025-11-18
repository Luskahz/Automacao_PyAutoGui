
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

from utilitarios.utils_global import ( 
    MAPA_ROTINAS,
    marcacao
)
from utilitarios.utils_promax import(
    MESES,
    EXT,
    exportar_csv,
    renomear_arquivo,
    fechar_janelas,
    acessar_rotina,
    movimentacao_arquivo_sql,
    inserir_datas,
    janela_contem_texto,
    janela_aberta,
    focar_janela
    
)


def promax(metadado, usuario, senha, formato):
    print("metadado de interface promax")

    if(metadado["periodo"]) == "diario":
        datas = metadado["datas"] 
    match metadado["periodo"]:
        case "mensal":
            relatorio_mensal(usuario, senha, formato, metadado)
        case "diario":
            arquivo_diario(usuario, senha, formato, metadado, datas )

def relatorio_mensal(usuario, senha, formato, metadado):
    agora = datetime.now()
    nome_pos_promax = f"{MESES[agora.month]}_{metadado["rotina"]}.{EXT}"

    # -------------------------------
    # LOGIN
    # -------------------------------
    if formato == "especifico":
        login_promax(usuario, senha)


    # -------------------------------
    # EXECUÇÃO DA ROTINA
    # -------------------------------
    print("identificando tela de rotinas do promax")
    while janela_contem_texto(["Promax 12.17.00.00 - 008-0001-R IMARUI LESTE DIST. E LOGISTICA LTDA.", "cadastramentos", "controle", "estoque", "B2B", "OBZ"], "PromaxWEB") is not True:
        time.sleep(0.1)
        print("tentando novamente...")
    print("tela de rotinas identificada...")
    acessar_rotina(metadado["rotina"])
    while janela_aberta(f"{usuario}"+" - "+f"{usuario}") is not True:
        time.sleep(0.3)
        print("abrindo formulario")
    print("formulário rotina carregado")
    metadado["sequencia_inicio_ate_data"]()
    inserir_datas(metadado["data_inicio"], metadado["data_final"])
    metadado["sequencia_data_ate_final"]()
    while janela_aberta("Processando") is not False:
        time.sleep(0.01)
        print("processando")
    # -------------------------------
    # EXPORTAÇÃO E RENOMEAÇÃO
    # -------------------------------

    while janela_contem_texto(["csv", "osv", "salvar", "anterior"], metadado["janelas_popup"][1]) is not True:
        time.sleep(1)
        print("procurando o botão de salvar CSV")
    exportar_csv(metadado["janelas_popup"][1])
    renomear_arquivo(nome_pos_promax)

    # -------------------------------
    # MOVIMENTAÇÃO E LIMPEZA
    # -------------------------------
    movimentacao_arquivo_sql(nome_pos_promax, agora, metadado)
    fechar_janelas(metadado["janelas_popup"])

    print(f"✅ Extração {metadado["rotina"]} concluída com sucesso.")

def arquivo_diario(usuario, senha, formato, metadado, datas):
    dia = datetime.strptime(datas["d1"], "%d/%m/%Y").day
    agora = datetime.now()
    nome_pos_promax = f"{str([agora.day])}_{metadado["rotina"]}.{EXT}"
    
    # -------------------------------
    # LOGIN
    # -------------------------------
    if formato == "especifico":
        login_promax(usuario, senha)
        for _ in range(5):
            pyautogui.press("tab")

    # -------------------------------
    # EXECUÇÃO DA ROTINA
    # -------------------------------
    print("identificando tela de rotinas do promax")
    inicio_promax = janela_contem_texto("Promax 12.17.00.00 - 008-0001-R IMARUI LESTE DIST. E LOGISTICA LTDA.", "PromaxWEB")
    while inicio_promax is not True:
        time.sleep(0.2)
        inicio_promax = janela_contem_texto("Promax 12.17.00.00 - 008-0001-R IMARUI LESTE DIST. E LOGISTICA LTDA.", "PromaxWEB")
        print("tentando novamente...")
    print("tela de rotinas identificada...")
    acessar_rotina(metadado["rotina"])
    while janela_aberta(f"{usuario}"+" - "+f"{usuario}") is not True:
        time.sleep(0.3)
        print("abrindo formulario")
    print("formulário rotina carregado")
    metadado["sequencia_inicio_ate_data"]()
    inserir_datas(metadado["datas"]["d1"], metadado["datas"]["d1"])
    metadado["sequencia_data_ate_final"]()
    while janela_contem_texto(["Arquivo", "gerado","sucesso"], metadado["janelas_popup"][1]) is not True:
        time.sleep(2)
        print("aguardando gerar o arquivo")
    pyautogui.press('enter')
    fechar_janelas(metadado["janelas_popup"][1])
    # -------------------------------
    # EXPORTAÇÃO E RENOMEAÇÃO
    # -------------------------------
    focar_janela("PromaxWEB")
    
    janela = gw.getActiveWindow()
    cx = janela.left + janela.width // 2
    cy = janela.top + janela.height // 2

    pyautogui.click(cx, cy)
    pyautogui.hotkey('shift', 'f10')
    for _ in range(13):
        pyautogui.press("down")
    pyautogui.press('enter')
    focar_janela("PP00100")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    
    conteudo = pyperclip.paste()


    match = re.search(r'SessionID2 value="([^"]+)"', conteudo)
    if match:
        session_id = match.group(1)
    print("SESSION:", session_id)
    url_sessao = f"http://imarui.promaxcloud.com.br:8080/?sessionId={session_id}"
    subprocess.Popen(["start", "msedge", url_sessao], shell=True)
    time.sleep(1)
    link_importacao = (
    "http://imarui.promaxcloud.com.br:8080/"
    + metadado["caminho_extracao"]
    + str(dia)
    + metadado["extencao_extracao"]
    )
        
    subprocess.Popen(["start", "msedge", link_importacao], shell=True)
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    subprocess.Popen(f'explorer "{downloads}"')
    # -------------------------------
    # MOVIMENTAÇÃO E LIMPEZA
    # -------------------------------
    movimentacao_arquivo_sql(nome_pos_promax, agora, metadado)
    fechar_janelas(metadado["janelas_popup"])

    print(f"✅ Extração {metadado['rotina']} concluída com sucesso.")

