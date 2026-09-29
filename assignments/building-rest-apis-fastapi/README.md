# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST simples com FastAPI para praticar criação de rotas HTTP, parâmetros de caminho, validação de dados com Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Criar a aplicação e uma rota de saúde

#### Descrição

Use o arquivo `starter-code.py` como ponto de partida. Instale as dependências com `pip install fastapi uvicorn` e execute a aplicação com `python starter-code.py`. A documentação interativa ficará disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI com o título `Books API`.
- Implementar `GET /health` para retornar `{"status": "ok"}`.
- Iniciar o servidor local na porta `8000` quando o arquivo for executado diretamente.

### 🛠️ Implementar rotas para consultar livros

#### Descrição

Use a lista de livros em memória do código inicial para permitir que clientes consultem todos os livros ou busquem um livro pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books` para retornar a lista de livros.
- Implementar `GET /books/{book_id}` para retornar o livro com o identificador informado.
- Responder com HTTP `404 Not Found` quando o identificador não corresponder a nenhum livro.

### 🛠️ Adicionar livros à coleção

#### Descrição

Permita que clientes enviem os dados de um livro em JSON para adicioná-lo à coleção em memória.

#### Requisitos

O programa concluído deve:

- Implementar `POST /books` recebendo `title` e `author` no corpo da requisição.
- Usar um modelo Pydantic para validar os dados recebidos.
- Gerar um identificador para o novo livro e adicioná-lo à lista em memória.
- Retornar o livro criado com HTTP `201 Created`.
- Permitir testar as rotas pela documentação interativa em `/docs`.