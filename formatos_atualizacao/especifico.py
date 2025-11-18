from interfaces.interface_barrier import identificar_interface
from utilitarios.utils_global import (
    MAPA_ROTINAS,
    obter_metadados
    
)

def especifico(formato, base):
    if base is None:
        rotina_usuario = input("Insira a base para atualização: ")
        print("iniciando atualização da base: " + rotina_usuario )
        identificar_interface(obter_metadados(rotina_usuario), formato)
    else:
        print("Atualizando base: "+ base)
        identificar_interface(obter_metadados(base), formato)

    

