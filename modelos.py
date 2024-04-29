from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db= SQLAlchemy()

class Usuario(db.Model):
    __tablename__= 'user'
    
    id_user= db.Column(db.Integer, primary_key=True)
    nombre_y_apellido= db.Column(db.String(30))
    email=db.Column(db.String(20))
    contrasenha=db.Column(db.String(10))
