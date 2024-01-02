import requests
import json
import time
import os


diretorio_saida = r"xxx"

def consultar_e_salvar(cnpj, diretorio_saida):
    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

    resp = requests.get(url)

    if resp.status_code == 200:
        json_data = resp.json()
        caminho_saida = os.path.join(diretorio_saida, f"{cnpj}.json")
        with open(caminho_saida, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        print(f"JSON para CNPJ {cnpj} salvo em {caminho_saida}.")
    else:
        print(f"Falha na solicitação para CNPJ {cnpj}. Código de status: {resp.status_code}")

arquivo_path = os.path.join("mes", "10.txt")

with open(arquivo_path, "r", encoding="utf-8") as arquivo:
    for indice, linha in enumerate(arquivo, start=1):
        cnpj = linha.strip()
        consultar_e_salvar(cnpj, diretorio_saida)

        if indice % 3 == 0:
            print("Esperando 1:15 minutos...")
            time.sleep(75)
