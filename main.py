from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
import models 
from models import Person

app = FastAPI()


@app.get("/student/{id}")
def get_user(id: int, db: Session = Depends(database.get_db)):
    data = db.query(models.student).filter(models.student.id == id).first()
    return {"data": data}

    #127.0.0.1:8000/person
@app.post("/person")
def add_person(username: str,
    password:str,
    email:str,
    blog_id:int,
    db: Session = Depends(database.get_db)):
        data = Person(person_username = username, person_password = password, person_email = email, blog_id = blog_id)
        db.add(data)
        db.commit()
        return {"status": 201, "message": "Data added sucessfully", "data":data}

@app.get("person/{id}")
def get_person_by_id(id:int,db:Session = Depends(database.get_db)):
    data = db.query(models.Person).filter(models.Person.id == id).first()
    return {"status": 200, "message": "Data Found", "data":data}

