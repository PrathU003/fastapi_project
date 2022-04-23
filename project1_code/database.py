from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BD_URL = 'postgresql://admin:admin@Localhost/project'            #todos.db is db file name

engine = create_engine(
    BD_URL 
)

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)


Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
