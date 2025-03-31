import zipfile


CSV_FILE = "rol_procedimentos.csv"
ZIP_FILE = "Teste_Thiago.zip"


with zipfile.ZipFile(ZIP_FILE, "w") as zipf:
    zipf.write(CSV_FILE)

print(f"✅ Arquivo ZIP criado: {ZIP_FILE}")

