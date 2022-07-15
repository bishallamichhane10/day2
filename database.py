from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABE_URL = "mysql+pymysql://root@localhost:3306/day2"
engine = create_engine(SQLALCHEMY_DATABE_URL)

SessionLocal = sessionmaker(bind= engine, autocommit=False, autoflush=False, )


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()