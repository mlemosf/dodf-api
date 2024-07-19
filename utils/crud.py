# Operações de crud

from sqlalchemy.orm import Session
from utils import models, schemas

def get_user_by_api_key(db: Session, api_key : str):
    return db.query(models.User).filter(models.User.api_key == api_key).first()
