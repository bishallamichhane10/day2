from sqlalchemy import Column,MetaData,Integer
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
MetaData = MetaData()

class student(base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key = True, index = True)
    first_name = Column('first name',NullType)
    last_name = Column ('last name',NullType)
    dob = Column('dob',NullType)

class Person(base):
    __tablename__='table_person'
    id = Column(Integer,primary_key = True, index = True)
    person_username = Column('username', NullType)
    person_password = Column('password',NullType)
    person_email = Column('email',NullType)
    blog_id = Column('blog_id',NullType)


