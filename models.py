from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String
# setup a base class from all our models will inherit from
Base = declarative_base()

# setup a model
# we must provide the table via an attribute called __tablename__
# we must provide at east one column via class attributes
class Student(Base): # class definition
    __tablename__ = "students" # class attribute
    
    id = Column(Integer(),primary_key=True) # class attribute for column id