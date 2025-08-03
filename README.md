# Flask CRUD App

Este é um projeto muito simples de CRUD bobo e bem mal feito usando Flask e SQLAlchemy.

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone <URL-do-repositorio>
   cd crud
   ```

2. **Crie e ative um ambiente virtual (opcional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install flask flask_sqlalchemy click
   ```

4. **Defina a variável de ambiente do Flask:**
   ```bash
   export FLASK_APP=app.py
   ```

5. **Inicialize o banco de dados:**
   ```bash
   flask init-db
   ```

6. **Rode o servidor Flask:**
   ```bash
   flask run
   ```

7. **Acesse o app no navegador:**
   ```
   http://localhost:5000
   ```

