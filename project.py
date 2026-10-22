from fastapi import FastAPI, status, Depends
from fastapi import HTTPException
from typing import Optional
from pydantic import BaseModel
from database import get_db,engine
from sqlalchemy.orm import Session
from datetime import date
import model

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: date
    
@app.post("/books")
def create_book(book: Book, db: Session = Depends(get_db)):
    new_book = model.Book(id=book.id, title=book.title, author=book.author, publish_date=book.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(model.Book).all()
    return books

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    existing_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    existing_book.id = book.id
    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.publish_date = book.publish_date
    db.commit()
    db.refresh(existing_book)
    return existing_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    existing_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(existing_book)
    db.commit()
    return {"message": f"Book with ID {book_id} deleted successfully"}