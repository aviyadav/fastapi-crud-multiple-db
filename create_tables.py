from db import engine1, engine2
from models import Base1, Base2

Base1.metadata.create_all(bind=engine1)
Base2.metadata.create_all(bind=engine2)