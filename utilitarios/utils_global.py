import pyautogui, time, calendar, re
from datetime import datetime, timedelta
from utilitarios.utils_promax import(
    write_lower
)


def metadados_03_02_24(agora: datetime):
    def sequencia_inicio_ate_data():
        time.sleep(2)
        write_lower('mapa')
        pyautogui.press('enter')
        for _ in range(7): pyautogui.press('tab')
        pyautogui.press('right')
        for _ in range(2): pyautogui.press('tab')
        pyautogui.press('space')
        for _ in range(6): pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        for _ in range(7):
            pyautogui.press('tab')
        pyautogui.press('enter')
    return {
        "rotina": "03_02_24",
        "interface": "promax",
        "periodo": "mensal",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_02_24",
        "data_inicio": agora.replace(day=1).strftime("%d/%m/%Y"),
        "data_final": datetime(
            agora.year, agora.month, calendar.monthrange(agora.year, agora.month)[1]
        ).strftime("%d/%m/%Y"),
        "janelas_popup": ["Downloads", "Rel. de Notas Devolvidas", "PromaxWeb"  ],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao,
    }

def metadados_03_11_40(agora: datetime):
    def sequencia_inicio_ate_data():
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        for _ in range(7):
            pyautogui.press('tab')
        pyautogui.press('enter')

    return {
        "rotina": "03_11_40",
        "interface": "promax",
        "periodo": "mensal",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_11_40",
        "data_inicio": agora.replace(day=1).strftime("%d/%m/%Y"),
        "data_final": datetime(
            agora.year,
            agora.month,
            calendar.monthrange(agora.year, agora.month)[1]
        ).strftime("%d/%m/%Y"),
        "janelas_popup": ["Downloads", "Rel. Tempos e Movimentos MPD", "PromaxWeb"],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao,
    }

def metadados_03_02_37_ope_vei_map(agora: datetime):
    def sequencia_inicio_ate_data():
        time.sleep(3)
        pyautogui.press('o')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('v')
        pyautogui.press('e')
        pyautogui.press('i')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('m')
        pyautogui.press('a')
        pyautogui.press('p')
        pyautogui.press('a')
        pyautogui.press('enter')
        for _ in range(3):
            pyautogui.press('tab')
        pyautogui.press('left')
        for _ in range(14):
            pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        for _ in range(10):
            pyautogui.press('tab')
        pyautogui.press('enter')

    return {
        "rotina": "03_02_37",
        "interface": "promax",
        "periodo": "mensal",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_02_37_operacao_veiculo_mapa",
        "data_inicio": agora.replace(day=1).strftime("%d/%m/%Y"),
        "data_final": datetime(
            agora.year,
            agora.month,
            calendar.monthrange(agora.year, agora.month)[1]
        ).strftime("%d/%m/%Y"),
        "janelas_popup": ["Downloads", "Rel. Notas Fiscais Plus", "PromaxWeb"],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao,
    }

def metadados_03_05_30_cl(agora: datetime):
    def sequencia_inicio_ate_data():
        time.sleep(3)
        pyautogui.press('c')
        pyautogui.press('enter')
        for _ in range(5):
            pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        for _ in range(23):
            pyautogui.press('tab')
        pyautogui.press('enter')

    return {
        "rotina": "03_05_30",
        "interface": "promax",
        "periodo": "mensal",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_05_30_cliente",
        "data_inicio": agora.replace(day=1).strftime("%d/%m/%Y"),
        "data_final": datetime(
            agora.year,
            agora.month,
            calendar.monthrange(agora.year, agora.month)[1]
        ).strftime("%d/%m/%Y"),
        "janelas_popup": ["Downloads", "Drop Size do Vendedor", "PromaxWeb"],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao,
    }

def metadados_03_05_30_mapa(agora: datetime):
    def sequencia_inicio_ate_data():
        time.sleep(3)
        pyautogui.press('m')
        pyautogui.press('a')
        pyautogui.press('p')
        pyautogui.press('a')
        pyautogui.press('enter')
        for _ in range(5):
            pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        for _ in range(23):
            pyautogui.press('tab')
        pyautogui.press('enter')

    return {
        "rotina": "03_05_30",
        "interface": "promax",
        "periodo": "mensal",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_05_30_mapa",
        "data_inicio": agora.replace(day=1).strftime("%d/%m/%Y"),
        "data_final": datetime(
            agora.year,
            agora.month,
            calendar.monthrange(agora.year, agora.month)[1]
        ).strftime("%d/%m/%Y"),
        "janelas_popup": ["Downloads", "Drop Size do Vendedor", "PromaxWeb"],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao,
    }

def metadados_03_11_29(agora: datetime):    
    def sequencia_inicio_ate_data():
        time.sleep(3)
        pyautogui.press('g')
        pyautogui.press('enter')
        pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        pyautogui.press('tab')
        pyautogui.press('enter')

    return {
        "rotina": "03_11_29",
        "interface": "promax",
        "periodo": "mensal",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_11_29",
        "data_inicio": agora.replace(day=1).strftime("%d/%m/%Y"),
        "data_final": datetime(
            agora.year,
            agora.month,
            calendar.monthrange(agora.year, agora.month)[1]
        ).strftime("%d/%m/%Y"),
        "janelas_popup": ["Downloads", "Escala de Equipe", "PromaxWeb"],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao,
    }

def metadados_03_08_05(agora: datetime):

    def sequencia_inicio_ate_data():
        time.sleep(3)
        pyautogui.press('c')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')

    def sequencia_data_ate_exportacao():
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

    return {
        "rotina": "03_08_05",
        "interface": "promax",
        "dias_periodo": 1,
        "periodo": "diario",
        "caminho_sql": r"Distribuição Urbana\rotinas\03_08_05",
        "datas": {
            "d1": (
                (agora - timedelta(days=2)) 
                if agora.weekday() == 0 
                else (agora - timedelta(days=1))
            ).strftime("%d/%m/%Y")
        },
        "caminho_extracao": "arquivos/download/file/dvs/2artd",
        "extencao_extracao": "_0001.txt",
        "nome_exportacao": "2artd",
        "janelas_popup": ["Downloads", "Remuneração de Transportadora", "PP00100", "Gerenciador de Arquivos", "PromaxWeb"],
        "sequencia_inicio_ate_data": sequencia_inicio_ate_data,
        "sequencia_data_ate_final": sequencia_data_ate_exportacao
    }


MAPA_ROTINAS = {
    "03_11_40": {
        "metadado": metadados_03_11_40,
        "nomes_alternativos": [
            "031140", "03_11_40", "03-11-40", "03.11.40", "31140",
        ],
    },

    "03_02_24": {
        "metadado": metadados_03_02_24,
        "nomes_alternativos": [
            "03_02_24", "302024", "03.02.24", "03-02-24",
            "03 02 24", "30224", "03_0224",
        ],
    },

    "03_05_30_cl": {
        "metadado": metadados_03_05_30_cl,
        "nomes_alternativos": [
            "03_05_30_cl", "30530cl", "03.05.30cl",
            "03-05-30cl", "03_05_30_cliente",
            "30530_cliente", "30530-cl",
        ],
    },

    "03_05_30_mapa": {
        "metadado": metadados_03_05_30_mapa,
        "nomes_alternativos": [
            "03_05_30_mapa", "30530mapa", "03.05.30mapa",
            "30530_mapa", "30530-map",
        ],
    },

    "03_02_37_ope_vei_map": {
        "metadado": metadados_03_02_37_ope_vei_map,
        "nomes_alternativos": [
            "03_02_37_ope_vei_map", "30237map",
            "03.02.37_map", "03-02-37-map",
            "30237_map", "03_0237map",
        ],
    },

    "03_11_29": {
        "metadado": metadados_03_11_29,
        "nomes_alternativos": [
            "03_11_29", "03-11-29", "03.11.29", "31129", "031129",
        ],
    },

    "03_08_05": {
        "metadado": metadados_03_08_05,
        "nomes_alternativos": [
            "03_08_05", "03-08-05", "03.08.05", "30805", "030805",
        ],
    },

    # Por enquanto esses ainda não têm metadados com fluxo de pyautogui,
    # então mantive só nomes_alternativos. Quando você criar metadados_bees_deliver,
    # é só adicionar o "metadado": metadados_bees_deliver aqui.
    "bees_deliver": {
        "nomes_alternativos": [
            "bees", "beesdeliver", "bees_deliver",
            "bees-deliver", "bdlvr",
        ],
    },

    "roteirizador": {
        "nomes_alternativos": [
            "roteirizador", "rot", "rtz", "route", "rotz", "roteiro",
        ],
    },

    "boletim_do_veiculo": {
        "nomes_alternativos": [
            "boletim_do_veiculo", "bdv", "boletim_veiculo",
            "boletim-veiculo", "boletimveiculo",
        ],
    },

    "historico_detalhado": {
        "nomes_alternativos": [
            "historico_detalhado", "historico", "hist_det",
            "histdetalhado", "historico-detalhado",
        ],
    },

    "relatorio_separacao": {
        "nomes_alternativos": [
            "relatorio_separacao", "relatorio-separacao",
            "relatorio_sep", "rseparacao", "wms_sep",
        ],
    },

    "qlp": {
        "nomes_alternativos": [
            "qlp", "quality", "qualidade", "q_l_p", "q-l-p",
        ],
    },
}



def normalizar(texto: str) -> str:
    """
    Remove espaços, símbolos comuns e deixa lowercase.
    Garante que '03-02-24', '03_02_24', '030224' fiquem comparáveis.
    """
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]", "", texto)
    return texto

def identificar_rotina(busca: str, mapa: dict) -> str | None:
    """
    Recebe uma string e procura nos nomes alternativos de todas as rotinas.
    Retorna o nome oficial da rotina ou None se não encontrar.
    """
    busca_norm = normalizar(busca)

    for rotina, dados in mapa.items():
        for alt in dados.get("nomes_alternativos", []):
            if normalizar(alt) == busca_norm:
                return rotina

    return None

def marcacao(tempoSegundos):
    print("codigo chegou a este ponto")
    time.sleep(tempoSegundos)

def obter_metadados(busca: str) -> dict | None:
    rotina = identificar_rotina(busca, MAPA_ROTINAS)
    if rotina is None:
        return None

    entrada = MAPA_ROTINAS[rotina]          
    fn_metadado = entrada["metadado"]       

    agora = datetime.now()
    metadados = fn_metadado(agora)       

    return metadados