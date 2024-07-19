# Models de banco de dados para os usuários

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from utils.db import Base

class User(Base):
    """
    Classe de usuários
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    api_key = Column(String)
    is_active = Column(Boolean, default=False)

    
