from fastapi import FastAPI, HTTPException
from models import Book

app = FastAPI()

books = [
    {
        "id": 1,
        "name": "Manipulyatsiya",
        "author": "Deyl Karnegi"
    },
    {
        "id": 2,
        "name": "O'lsang kim yig'laydi",
        "author": "Robin Sharma"
    },
    {
        "id": 3,
        "name": "Liderlik shaxsiyati",
        "author": "Brayan Treysi"
    }
]

@app.get("/books/", tags=['📖 Kitoblar'], summary='Barcha kitoblar royxati')
def get_books():
    return books

@app.get("/book/{book_id}/", tags=['📖 Kitoblar'], summary='Idga mos kitob')
def get_book(book_id: int):
    for book in books:
        if book_id == book["id"]:
            return book   
    raise HTTPException(status_code=404, detail="Not Found")

@app.post("/book/update/", tags=['📖 Kitoblar'], summary="Yangi kitob qo'shish")
def update_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "name": book.name,
        "author": book.author
    }
    books.append(new_book)
    return new_book