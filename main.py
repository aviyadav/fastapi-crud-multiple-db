from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import get_db1, get_db2
from models import User1, User2
from schemas import User, UserCreate, UserUpdate

app = FastAPI()

# Create a user
@app.post("/db1/users", response_model=User)
def create_user_db1(user: UserCreate, db: Session = Depends(get_db1)):
    db_user = User1(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/db2/users/", response_model=User)
def create_user_db2(user: UserCreate, db: Session = Depends(get_db2)):
    db_user = User2(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Read Users
@app.get("/db1/users/", response_model=List[User])
def read_users_db1(skip: int = 0, limit: int = 10, db: Session = Depends(get_db1)):
    users = db.query(User1).offset(skip).limit(limit).all()
    return users

@app.get("/db2/users/", response_model=List[User])
def read_users_db2(skip: int = 0, limit: int = 10, db: Session = Depends(get_db2)):
    users = db.query(User2).offset(skip).limit(limit).all()
    return users

# Update a User
@app.put("/db1/users/{user_id}", response_model=User)
def update_user_db1(user_id: int, user: UserUpdate, db: Session = Depends(get_db1)):
    db_user = db.query(User1).filter(User1.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/db2/users/{user_id}", response_model=User)
def update_user_db2(user_id: int, user: UserUpdate, db: Session = Depends(get_db2)):
    db_user = db.query(User2).filter(User2.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# Delete a User
@app.delete("/db1/users/{user_id}", response_model=User)
def delete_user_db1(user_id: int, db: Session = Depends(get_db1)):
    db_user = db.query(User1).filter(User1.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user

@app.delete("/db2/users/{user_id}", response_model=User)
def delete_user_db2(user_id: int, db: Session = Depends(get_db2)):
    db_user = db.query(User2).filter(User2.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user