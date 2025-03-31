import requests
from bs4 import BeautifulSoup
import os


URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


PASTA_DOWNLOADS = "downloads"
os.makedirs(PASTA_DOWNLOADS, exist_ok=True)

def baixar_pdf(url, nome_arquivo):
   
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        caminho_arquivo = os.path.join(PASTA_DOWNLOADS, nome_arquivo)
        with open(caminho_arquivo, "wb") as f:
            for chunk in resposta.iter_content(1024):
                f.write(chunk)
        print(f"✅ PDF salvo: {caminho_arquivo}")
    else:
        print(f"❌ Erro ao baixar {nome_arquivo}")


resposta = requests.get(URL)
soup = BeautifulSoup(resposta.text, "html.parser")


links_pdf = []
for link in soup.find_all("a", href=True):
    if "Anexo" in link.text and link["href"].endswith(".pdf"):
        links_pdf.append((link.text.strip(), link["href"]))


if links_pdf:
    for nome, link in links_pdf:
        baixar_pdf(link, f"{nome}.pdf")
else:
    print("❌ Nenhum PDF encontrado.")
