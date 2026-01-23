from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine,Integer,Column,String
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel

URL = "postgresql://postgres:tarun@localhost:5432/gamma_db"

engine = create_engine(URL)

sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()



class Books(Base):
    __tablename__ = 'Books'
    bookId = Column(Integer,primary_key=True)
    bookName = Column(String,nullable=False)
    author = Column(String)

class BookSchema(BaseModel):
    bookId:int
    bookName:str
    author:str

Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/book")
def get_books(db:Session=Depends(get_db)):
    books = db.query().all()
    return books
def add_books(request:BookSchema, db:Session=Depends(get_db)):
    book = BookSchema(bookId=request.id,bookName=request.name,author=request.author)
    db.add(book)
    db.commit()
    