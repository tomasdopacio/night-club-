from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comidas(db.Model):
    __tablename__ = "comidas"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integer, nullable = False)

class Bebidas(db.Model):
    __tablename__ = "bebidas"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integer, nullable = False)

class Tragos(db.Model):
    __tablename__ = "tragos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integer, nullable = False)

class Combos(db.Model):
    __tablename__ = "combos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    id_comida = db.Column(db.Integer, db.ForeignKey("comidas.id"))
    id_bebida = db.Column(db.Integer, db.ForeignKey("bebidas.id"))
    id_tragos = db.Column(db.Integer, db.ForeignKey("tragos.id"))