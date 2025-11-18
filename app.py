import schedule
import time
import os
import threading
from queue import Queue

from formatos_atualizacao.automatico import automatico
from formatos_atualizacao.especifico import especifico


# ======================================================
# FILA CENTRAL E WORKER ÚNICO
# ======================================================

fila = Queue()
executando = False


def worker():
    global executando

    while True:
        tarefa = fila.get()   
        formato, base = tarefa

        executando = True
        try:
            if formato == "automatico":
                automatico(formato)
            else:
                especifico(formato, base)
        except Exception as e:
            print(f"\n❌ Erro executando tarefa [{formato} | {base}]: {e}")
        finally:
            executando = False
            fila.task_done()



threading.Thread(target=worker, daemon=True).start()


# ======================================================
# FUNÇÕES UTILITÁRIAS
# ======================================================

def enfileirar_tarefa(formato, base=None):
    """Coloca qualquer tarefa na fila única."""
    fila.put((formato, base))
    print(f"\n📌 Tarefa '{formato} {base}' adicionada à fila.")


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


# ======================================================
# SCHEDULER
# ======================================================

schedule.every().day.at("07:30").do(enfileirar_tarefa, "automatico")
schedule.every(15).minutes.do(enfileirar_tarefa, "especifico", "03_11_40")
schedule.every(60).minutes.do(enfileirar_tarefa, "especifico", "03_01_47_01")
threading.Thread(target=run_scheduler, daemon=True).start()


# ======================================================
# MENU
# ======================================================

def exibir_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n===========================================")
    print("Processo de atualização dos dados do SQL")
    print("===========================================")
    print("Bases que serão atualizadas:")
    print("03_11_40, 03_02_24, 03_02_37, ...")
    print("")
    print("Configurações:")
    print("[1][auto] - Automática")
    print("[2][espec] - Por base específica")
    print("[0] - Sair")


if __name__ == "__main__":
    aliases = {
        "1": "automatico",
        "auto": "automatico",
        "2": "especifico",
        "espec": "especifico",
    }

    while True:
        exibir_menu()
        formato_raw = input("Selecione: ").strip().lower()
        formato = aliases.get(formato_raw, formato_raw)

        if formato == "automatico":
            enfileirar_tarefa("automatico")

        elif formato == "especifico":
            base = input("Qual base? ").strip()
            enfileirar_tarefa("especifico", base)

        elif formato in ("0", "sair", "exit", "quit"):
            print("Encerrando...")
            break

        else:
            print("❌ Opção inválida.")

        input("\nPressione Enter para voltar ao menu...")
