from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base 

# entidade Users
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Integer, nullable=False)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    
    # para mostrar masi bonito os dados quando for printar
    def __repr__(self):
        return f"User[id={self.id!r}, first_name={self.first_name}]"