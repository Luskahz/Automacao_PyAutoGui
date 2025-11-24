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
ultima_tarefa = None


def worker():
    print("DEBUG: Worker iniciado!")
    global executando, ultima_tarefa

    while True:
        print("DEBUG: Worker esperando tarefa...")
        tarefa = fila.get()
        print(f"DEBUG: Worker recebeu tarefa -> {tarefa}")

        formato, base = tarefa

        executando = True
        ultima_tarefa = f"{formato} {base}"
        print(f"DEBUG: Executando tarefa: formato={formato}, base={base}")

        try:
            if formato == "automatico":
                print("DEBUG: Chamando automatico()...")
                automatico(formato)
                print("DEBUG: automatico() finalizou.")

            else:
                print(f"DEBUG: Chamando especifico({formato}, {base})...")
                especifico(formato, base)
                print("DEBUG: especifico() finalizou.")

        except Exception as e:
            print(f"\n❌ Erro executando tarefa [{formato} | {base}]: {e}")
        finally:
            executando = False
            fila.task_done()
            print("DEBUG: tarefa concluída.")



# Inicia o worker
threading.Thread(target=worker, daemon=True).start()


# ======================================================
# UTILITÁRIAS
# ======================================================

def enfileirar_tarefa(formato, base=None):
    print(f"DEBUG: adicionando tarefa na fila -> ({formato}, {base})")
    fila.put((formato, base))
    print(f"\n📌 Tarefa '{formato} {base}' adicionada à fila.")
    print(f"DEBUG: Tamanho atual da fila = {fila.qsize()}")


def run_scheduler():
    print("DEBUG: Scheduler iniciado!")
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
# MENU + STATUS
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
    print("-------------------------------------------")
    print("STATUS DO SISTEMA:")
    print(f"• Executando agora: {ultima_tarefa if executando else 'Nenhuma'}")
    print(f"• Tarefas na fila: {fila.qsize()}")
    print("-------------------------------------------")


# ======================================================
# MAIN LOOP
# ======================================================

if __name__ == "__main__":
    print("DEBUG: Programa iniciado!")

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

        print(f"DEBUG: Usuário escolheu: {formato_raw} -> {formato}")

        if formato == "automatico":
            enfileirar_tarefa("automatico")

        elif formato == "especifico":
            base = input("Qual base? ").strip()
            print(f"DEBUG: Base escolhida: {base}")
            enfileirar_tarefa("especifico", base)

        elif formato in ("0", "sair", "exit", "quit"):
            print("Encerrando...")
            break

        else:
            print("❌ Opção inválida.")

        input("\nPressione Enter para voltar ao menu...")
