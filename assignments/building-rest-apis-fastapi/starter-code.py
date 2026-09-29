from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books = [
    Book(id=1, title="A Ilha", author="Ana Costa"),
    Book(id=2, title="O Caminho", author="Rui Martins"),
]


# TODO: Implemente GET /health.

# TODO: Implemente GET /books e GET /books/{book_id}.

# TODO: Implemente POST /books para criar um livro.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)