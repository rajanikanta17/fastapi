from sqlalchemy import Column, Integer,VARCHAR, String, Date
from database import Base, engine

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(255), nullable=False)
    author = Column(String(255), nullable=False)
    publish_date = Column(Date, nullable=False)