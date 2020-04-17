

'''

'''

from sqlalchemy import Column, Integer, DECIMAL, String, Date, Text,
from ..db import Base

class UserModel(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    dob = Column(Date, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(Text, nullable=False)
