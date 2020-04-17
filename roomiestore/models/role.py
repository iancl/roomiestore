from ..db import Base
from sqlalchemy import Text, Column, SmallInteger


class Role(Base):
    __tablename__ = 'role'
    role_id = Column(SmallInteger, primary_key=True)
    name = Column(Text(length=50), nullable= False, unique=True)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f'Role({self.name, self.role_id})'


