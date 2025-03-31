import pandas as pd

CSV_FILE = "rol_procedimentos.csv"


substituicoes = {
    "OD": "Odontológico",
    "AMB": "Ambulatorial"
}


df = pd.read_csv(CSV_FILE)


df.replace(substituicoes, inplace=True)


df.to_csv(CSV_FILE, index=False)


print(f"✅ Abreviações substituídas com sucesso em {CSV_FILE}!")
