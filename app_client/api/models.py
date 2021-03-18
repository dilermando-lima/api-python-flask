from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Client(db.Model):
    id: int
    name: str
    email: str
    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
