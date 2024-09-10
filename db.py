from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL_1, DATABASE_URL_2

engine1 = create_engine(DATABASE_URL_1)
engine2 = create_engine(DATABASE_URL_2)

SessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine1)
SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine2)

def get_db1():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()


def get_db2():
    db = SessionLocal2()
    try:
        yield db
    finally:
        db.close()