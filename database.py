from sqlalchemy import create_engine,Integer, String,Column
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI,Depends
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:tarun@localhost:5432/gammaedge_db"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String,index=True)

class UserSchema(BaseModel):
    id:int
    name:str

Base.metadata.create_all(bind=engine)

app=FastAPI()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"Home"}

@app.post("/user")
def add_user(request:UserSchema,db:Session=Depends(get_db)):
    user = User(id=request.id, name=request.name)
    try:
        db.add(user)
        db.commit()
    except Exception as e:
        return {e}
    db.refresh(user)
    return {
        "message":"Successfully Added",
        "user":user
    },201

@app.get("/users")
def get_user(user_id:int,db:Session=Depends(get_db)):
    
    user1 = db.query(User).filter(User.id == user_id).first()
    return user1
    
