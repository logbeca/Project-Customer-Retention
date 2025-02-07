from sqlalchemy import create_engine
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base  
from sqlalchemy.exc import SQLAlchemyError

SQLALCHEMY_DATABASE_URL =  "postgresql://user:password@postgres/mydatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo= True)

SessionLocal = sessionmaker(autocommit= False, autoflush = False, bind= engine)

Base =  declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        db.rollback()
        raise
    finally:
        db.close()

get_db()


