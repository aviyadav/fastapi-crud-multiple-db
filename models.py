from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base1 = declarative_base()
Base2 = declarative_base()

class User1(Base1):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class User2(Base2):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)