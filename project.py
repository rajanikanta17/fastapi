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