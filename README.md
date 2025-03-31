```
# 📊 Projeto Fullstack com Python + Flask + Vue.js

Este projeto é uma aplicação fullstack com back-end em **Python + Flask** e front-end em **Vue.js**. O sistema lê arquivos **CSV**, armazena dados em um banco **PostgreSQL**, e apresenta uma interface moderna e interativa para visualização e manipulação dos dados.

---

## 🚀 Tecnologias

- **Back-end:** Python, Flask, SQLAlchemy  
- **Banco de Dados:** PostgreSQL  
- **Front-end:** Vue.js  
- **Outros:** Pandas (para leitura dos CSVs)

---

## 📂 Estrutura do Projeto

```
.
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── package.json
│   ├── src/
│   └── ...
├── data/
│   └── seus_arquivos.csv
└── README.md
```

---

## ⚙️ Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
```

---

### 2. Configurar o Back-end

#### Pré-requisitos:

- Python 3.9+
- PostgreSQL instalado e rodando

#### Passos:

```bash
cd backend
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Crie o banco de dados no PostgreSQL:

```sql
CREATE DATABASE nome_do_banco;
```

#### Configure as variáveis de ambiente:

```bash
export DB_USER=seu_usuario
export DB_PASSWORD=sua_senha
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=nome_do_banco
```

> 💡 Dica: use um `.env` com [python-dotenv](https://pypi.org/project/python-dotenv/) se preferir.

#### Para rodar o back-end:

```bash
python app.py
```

---

### 3. Rodar o Front-end

#### Pré-requisitos:

- Node.js e npm instalados

```bash
cd frontend
npm install
npm run serve
```

---

## 📥 Importação de CSVs

- Coloque seus arquivos `.csv` na pasta `/data`
- O back-end cuidará da leitura e persistência no banco de dados automaticamente

---

## 🧪 Testes

> *(Se houver testes, adicione instruções aqui)*

---

## 🛠️ Contribuindo

Pull requests são bem-vindos! Sinta-se à vontade para abrir issues e sugerir melhorias.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## ✨ Autor

Feito com 💻 por [Seu Nome](https://github.com/seu-usuario)
```