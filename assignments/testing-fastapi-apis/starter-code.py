from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

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


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    next_id = max((existing_book.id for existing_book in books), default=0) + 1
    new_book = Book(id=next_id, title=book.title, author=book.author)
    books.append(new_book)
    return new_book