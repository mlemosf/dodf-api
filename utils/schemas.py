# Arquivo de schemas

from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    api_key : str
    is_active : bool

    class Config:
        from_attributes = True
