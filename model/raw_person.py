from sqlalchemy import Column, Integer, String, Date
from model import Base

class RawPerson(Base):
    __tablename__= "raw"
    id = Column('id', Integer, primary_key=True) 
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    address = Column(String(length=150))
    email = Column(String(length=50))
    dob = Column(Date)
    ethnicity = Column(String(length=20))
    education = Column(String(length=20))
