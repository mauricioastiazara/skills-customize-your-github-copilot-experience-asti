# 📘 Assignment: Testing FastAPI APIs with pytest

## 🎯 Objective

Escreva testes automatizados para uma API FastAPI usando pytest e `TestClient`. Você praticará como verificar respostas HTTP, validar entradas inválidas e manter cada teste independente.

## 📝 Tasks

### 🛠️ Preparar o ambiente de testes

#### Descrição

Copie `starter-code.py` para `main.py` no seu ambiente de trabalho e instale as dependências com `python -m pip install fastapi pytest httpx`. Crie um arquivo `test_main.py` para os testes e execute-os com `python -m pytest -q`.

#### Requisitos

O programa concluído deve:

- Importar a aplicação FastAPI de `main.py`.
- Criar um fixture pytest que forneça um `TestClient`.
- Preparar uma lista de livros conhecida para cada teste, sem deixar alterações de um teste afetarem outro.
- Executar a suíte com `python -m pytest -q`.

### 🛠️ Testar consultas e respostas HTTP

#### Descrição

Escreva testes para as rotas de saúde e consulta de livros. Verifique tanto o conteúdo das respostas quanto os códigos HTTP retornados.

#### Requisitos

O programa concluído deve:

- Verificar que `GET /health` retorna HTTP `200` e `{"status": "ok"}`.
- Verificar que `GET /books` retorna HTTP `200` e todos os livros preparados pelo fixture.
- Verificar que `GET /books/{book_id}` retorna HTTP `200` e os dados do livro solicitado.
- Verificar que buscar um identificador inexistente retorna HTTP `404`.

### 🛠️ Testar criação e validação de livros

#### Descrição

Teste a criação de livros e a validação do corpo da requisição. Use parametrização do pytest para cobrir mais de uma entrada inválida com o mesmo teste.

#### Requisitos

O programa concluído deve:

- Verificar que `POST /books` com `title` e `author` retorna HTTP `201` e o livro criado com um identificador.
- Confirmar que o livro criado aparece em uma consulta posterior a `GET /books`.
- Usar `pytest.mark.parametrize` para testar corpos sem `title` ou sem `author`.
- Verificar que cada corpo incompleto retorna HTTP `422 Unprocessable Entity`.