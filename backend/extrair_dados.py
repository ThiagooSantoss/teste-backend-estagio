import pdfplumber
import pandas as pd


PDF_PATH = "downloads/Anexo I..pdf"
CSV_PATH = "rol_procedimentos.csv"


with pdfplumber.open(PDF_PATH) as pdf:
    tabelas = []
    
    for page in pdf.pages:
        tabelas_extraidas = page.extract_tables()
        for tabela in tabelas_extraidas:
            tabelas.append(tabela)


df = pd.DataFrame([linha for tabela in tabelas for linha in tabela])


df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")


print(f"✅ Dados extraídos e salvos em: {CSV_PATH}")

