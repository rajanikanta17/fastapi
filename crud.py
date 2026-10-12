from fastapi import FastAPI,status
from fastapi import HTTPException
from typing import Optional
from pydantic import BaseModel

books=[
    {"id": 1, "title": "Book One", "author": "Author One", "publish_date": "2020-01-01"},
    {"id": 2, "title": "Book Two", "author": "Author Two", "publish_date": "2020-02-01"},
    {"id": 3, "title": "Book Three", "author": "Author Three", "publish_date": "2020-03-01"},
    {"id": 4, "title": "Book Four", "author": "Author Four", "publish_date": "2020-04-01"},
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str
    
@app.post("/books")
def create_book(book: Book):
    books.append(book.dict())
    return books

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publish_date: Optional[str] = None
    
@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookUpdate):
    for b in books:
        if b["id"] == book_id:
            if book.title is not None:
                b["title"] = book.title
            if book.author is not None:
                b["author"] = book.author
            if book.publish_date is not None:
                b["publish_date"] = book.publish_date
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            return {"message": f"Book with ID {book_id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")