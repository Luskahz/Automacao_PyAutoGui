import schedule, time, os
from formatos_atualizacao.automatico import automatico
from formatos_atualizacao.especifico import especifico

def exibir_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n===========================================")
    print("Iniciando processo de atualização dos dados do SQL...")
    print("===========================================")
    print("Bases que serão atualizadas:")
    print("03_11_40 -----------------------> M0")
    print("03_02_24 -----------------------> M0")
    print("03_02_37_operacão_veiculo_mapa -> M0")
    print("03_05_30_clientes --------------> M0")
    print("03_05_30_mensal ----------------> M0")
    print("03_11_29 -----------------------> M0")
    print("03_08_05 -----------------------> M0")
    print("Bees deliver -------------------> D1 e D0")
    print("Relatorio Roteirizador ---------> D1")
    print("QLP ----------------------------> D1")
    print("")
    print("Configurações de atualização:")
    print("[1][auto] - Automática")
    print("[2][espec] - Por base específica")
    print("[0][sair] - Sair")

def automacao(formato, base=None):
    match formato:
        case "automatico":
            try:
                automatico(formato)
            except Exception as e:
                print("\n❌ Erro durante a execução da rotina automática:\n" + e)

        case "especifico":
            try:
                especifico(formato, base)
            except Exception as e:
                print("\n❌ Erro durante a execução da rotina especifica:\n" + e)
    




if __name__ == "__main__":
    while True:
        try:
            exibir_menu()
            formato_raw = input("Selecione o formato de atualização: ").strip().lower()

            aliases = {
                "1": "automatico",
                "auto": "automatico",
                "2": "especifico",
                "espec": "especifico",
            }

            formato = aliases.get(formato_raw, formato_raw)


            if formato == "automatico":
                try:
                    automatico(formato)
                except Exception as e:
                    print("\n❌ Erro durante a execução da rotina automática:")
                    print(e)

            elif formato == "especifico":
                try:
                    especifico(formato)
                except Exception as e:
                    print("\n❌ Erro durante a execução da rotina específica:")
                    print(e)

            elif formato in ("0", "sair", "exit", "quit"):
                print("\nEncerrando...")
                break

            else:
                print("❌ Opção inválida, tente novamente.")

        except Exception as e:
            print("\n⚠️ Erro inesperado, mas o programa continuará rodando:")
            print(e)

        input("\nPressione Enter para voltar ao menu...")


schedule.every().day.at("07:30").do(automacao, "automatico")
schedule.every(15).minutes.do(automacao, "especifico", "03_11_40")
schedule.every(60).minutes.do(automacao, "especifico", "03_01_47_01")

while True:
    schedule.run_pending()
    time.sleep(5)