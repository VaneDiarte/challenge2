from flask import Flask
from modelos import db , Usuario

app= Flask('app')

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

with app.app_context():
    usuario_1 = Usuario
    usuario_2 = Usuario
    

    db.session.add(usuario_1)
    db.session.add(usuario_2)

    db.session.commit()



