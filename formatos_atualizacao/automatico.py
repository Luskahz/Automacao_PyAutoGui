from utilitarios.utils_global import MAPA_ROTINAS
from interfaces.interface_barrier import identificar_interface
from datetime import datetime

def automatico(formato):
    agora = datetime.now()

    for rotina, dados in MAPA_ROTINAS.items():
        if "metadado" in dados:
            fn = dados["metadado"]
            metadados = fn(agora)

            if "interface" in metadados:
                identificar_interface(metadados, formato)
