# calculator

# 🧮 Calculadora Avançada com Histórico (Django + HTML/CSS/JS)

Este projeto é uma calculadora avançada com autenticação de usuário, histórico de operações, e backend em Django. Foi desenvolvido como parte de um processo seletivo, focando em boas práticas, usabilidade e estrutura clara de código.

---

## 🔧 Tecnologias utilizadas

- **Backend**: Python + Django + Django REST Framework + JWT
- **Frontend**: HTML + CSS puro + JavaScript
- **Auth**: JSON Web Tokens (JWT)

---

## ✨ Funcionalidades

- 🧮 Cálculo de expressões matemáticas básicas (com múltiplos operadores)
- 🧑‍💻 Login e cadastro de usuários
- 💾 Histórico de operações com horário e resultado
- 🗑️ Botão de lixeira para apagar todo o histórico
- ✅ Evita expressões inválidas (ex: operadores duplicados)
- 📱 Responsivo para desktop e mobile
- 🔐 Proteção com autenticação (JWT)
  
---

## ▶️ Como rodar o projeto localmente

### 1. Clone o repositório

- git clone https://github.com/JonasNogueira/calculator.git
- cd seu-repositorio

### 2. Crie e ative um ambiente virtual

- python -m venv venv
- source venv/bin/activate  # ou venv\Scripts\activate no Windows

### 3. Instale as dependências

- pip install -r requirements.txt

### 4. Rode as migrações

- python manage.py migrate

### 5. Inicie o servidor

- python manage.py runserver

### 6. Acesse no navegador

- http://127.0.0.1:8000/login



## ▶️ Como acessar as rotas com o swagger

### 1. Acesse no navegador

- http://127.0.0.1:8000/swagger