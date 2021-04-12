from fastapi import Depends, Query
from typing import Optional, List

from ..db.database import SessionLocal



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()