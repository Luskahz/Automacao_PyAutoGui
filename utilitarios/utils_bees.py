import subprocess, json, time, os, base64 
from playwright.sync_api import sync_playwright


def fechar_processos_edge():
    processos = ["msedge.exe", "msedgedriver.exe"]
    for proc in processos:
        try:
            subprocess.run(
                ["taskkill", "/F", "/IM", proc],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except:
            pass
    print("Processos do Edge encerrados.")


def capturar_token_bees():
        fechar_processos_edge()
        time.sleep(5)
        os.makedirs("tokens", exist_ok=True)

        har_path = "tokens/captura.har"

        with sync_playwright() as p:

            browser = p.chromium.launch_persistent_context(
                user_data_dir=r"C:\Users\lucas.l\AppData\Local\Microsoft\Edge\User Data",
                headless=False,
                channel="msedge",
                record_har_path=har_path,
                record_har_content="embed"
            )

            page = browser.new_page()

            page.goto("https://deliver-portal.bees-platform.com/control-tower")
            time.sleep(5)

            try:
                page.locator("[data-test-id='download-btn']").click()
            except:
                print("Erro ao clicar no botão.")
                browser.close()
                return

            time.sleep(5)
            browser.close()

        # =====================================================
        #  PROCESSAR O HAR
        # =====================================================

        with open(har_path, "r", encoding="utf-8") as f:
            har = json.load(f)

        entrada_alvo = None

        for entry in har["log"]["entries"]:
            url = entry["request"]["url"]
            if "export-visits-data" in url:
                entrada_alvo = entry
                break

        if not entrada_alvo:
            print("Não encontrou a requisição no HAR.")
            return

        req = entrada_alvo["request"]
        res = entrada_alvo["response"]

        # Linha da requisição
        request_line = f"{req['method']} {req['url']} HTTP/1.1"

        # Linha da resposta
        response_line = f"HTTP/1.1 {res['status']} {res['statusText']}"

        # Headers em dict
        request_headers = {h["name"]: h["value"] for h in req["headers"]}
        response_headers = {h["name"]: h["value"] for h in res["headers"]}

        # Token
        auth = request_headers.get("authorization", "")
        token = None
        if auth.startswith("Bearer "):
            token = auth.replace("Bearer ", "")

        dados = {
            "token": token,
            "request_line": request_line,
            "request_headers": request_headers,
            "response_line": response_line,
            "response_headers": response_headers,
        }

        with open("tokens/bees.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print("Token e cabeçalhos salvos em tokens/bees.json")



def token_bees_valido(caminho="tokens/bees.json"):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        auth = dados["request_headers"].get("Authorization", "")

        if not auth.startswith("Bearer "):
            return False 

        token = auth.split(" ")[1] 

        partes = token.split(".")
        if len(partes) != 3:
            return False

        payload_b64 = partes[1]

        padding = len(payload_b64) % 4
        if padding != 0:
            payload_b64 += "=" * (4 - padding)

        payload_json = json.loads(base64.urlsafe_b64decode(payload_b64))

        exp = payload_json.get("exp")
        if exp is None:
            return False


        agora = int(time.time())


        return agora < exp

    except Exception as e:
        print("Erro ao validar token:", e)
        return False





