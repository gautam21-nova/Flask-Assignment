from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

# creating a database model for user table in our database using sqlalchemy orm
Base = declarative_base()

#table name in database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    role = Column(String(20))
