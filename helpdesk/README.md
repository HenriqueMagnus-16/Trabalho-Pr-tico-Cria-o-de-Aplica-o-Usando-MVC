# API Helpdesk

API desenvolvida em Python utilizando Flask, SQLAlchemy e SQLite.

## Arquitetura

O projeto utiliza arquitetura em camadas:

- Controllers
- Services
- Repositories
- Models

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite

## Instalação

Criar o ambiente virtual:

python -m venv venv

Ativar o ambiente virtual no Windows:

venv\Scripts\activate

Instalar as dependências:

pip install -r requirements.txt

## Execução

Executar:

python app.py

A API estará disponível em:

http://127.0.0.1:5000

O banco SQLite será criado automaticamente pela aplicação.

## Endpoints

### Usuários

GET /usuarios

POST /usuarios

PUT /usuarios/<id>

DELETE /usuarios/<id>

GET /usuarios/<id>/chamados

### Chamados

GET /chamados

POST /chamados

PUT /chamados/<id>

DELETE /chamados/<id>

PATCH /chamados/<id>/iniciar

PATCH /chamados/<id>/encerrar

GET /chamados/abertos

GET /chamados/prioridade/alta

### Estatísticas

GET /estatisticas

## Regras de negócio

- Nome obrigatório.
- E-mail obrigatório.
- E-mail não pode ser duplicado.
- Usuário com chamados não pode ser excluído.
- Título obrigatório.
- Título com pelo menos 5 caracteres.
- Descrição com pelo menos 10 caracteres.
- Chamado deve estar vinculado a usuário existente.
- Prioridade: Baixa, Média ou Alta.
- Status inicial: Aberto.
- Máximo de cinco chamados não encerrados por usuário.
- Status segue o fluxo:

Aberto -> Em atendimento -> Encerrado