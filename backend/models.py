from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comidas(db.Model):
    tablename = "comidas"
    id = db.Column(db.Inegrer, primarykey = True)
    name = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integrer, nullable = False)

class Bebidas(db.Model):
    tablename = "bebidas"
    id = db.Column(db.Integrer, primarykey = True)
    name = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integrer, nullable = False)

class Tragos(db.Model):
    _tablename = "tragos"
    id = db.Column(db.Integrer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integrer, nullable = False)

class Combos(db.Model):
    __tablename = "combos"
    id = db.Column(db.Inegrer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)
    precio = db.Column(db.Integrer, nullable = False)
    id_comida = db.Column(db.Integrer, db.ForeingKey("comidas.id"))
    id_bebida = db.Column(db.Integrer, db.ForeingKey("bebidas.id"))
    id_tragos = db.Column(db.Integrer, db.ForeingKey("tragos.id"))