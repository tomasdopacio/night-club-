from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Comidas, Bebidas, Tragos, Combos

app = Flask(__name__)
CORS(app)
port=5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://tomas:123456@localhost:5432/tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

@app.route("/")
def home():
    comidas = Comidas.query.all()
    """
    info_comidas = []
    info_de_comida = {
        "id_comida" : 1,
        "nombre" : "comida.nombre",
        "descripcion" : "comida.descripcion",
        "imagen" : "comida.imagen",
        "precio" : 10
    }
    info_comidas.append(info_de_comida)
    """
    bebidas = Bebidas.query.all()
    tragos = Tragos.query.all()
    combos = Combos.query.all()
    informacion_de_combos = []
    for combo in combos:
        info_combo = {
            "id" : combo.id,
            "nombre" : combo.nombre,
            "descripcion" : combo.descripcion,
            "imagen" : combo.imagen,
            "precio" : combo.precio
        }
        informacion_de_combos.append(info_combo)
    informacion_de_productos = {
        "comidas" : comidas,
        "bebidas" : bebidas,
        "tragos" : tragos,
        "combos" : informacion_de_combos
    }
    return jsonify(informacion_de_productos)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)