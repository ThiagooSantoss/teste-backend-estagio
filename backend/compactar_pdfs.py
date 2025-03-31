import zipfile
import os

PASTA_DOWNLOADS = "downloads"
ARQUIVO_ZIP = "anexos_compactados.zip"

with zipfile.ZipFile(ARQUIVO_ZIP, "w") as zipf:
    for arquivo in os.listdir(PASTA_DOWNLOADS):
        caminho_arquivo = os.path.join(PASTA_DOWNLOADS, arquivo)
        zipf.write(caminho_arquivo, arquivo)

print(f"✅ Arquivo ZIP criado: {ARQUIVO_ZIP}")
