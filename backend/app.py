from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Comidas, Bebidas, Tragos, Combos

app = Flask(__name__)
CORS(app)
port=5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://tp:tp@localhost:5432/tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



@app.route("/")
def home():
    try:
        comidas = Comidas.query.all()
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
    except:
        return {"error" : "errorDeServidor"} , 500

@app.route("/crear/<producto>", methods = ["POST"])
def crear_producto(producto):
    try:
        tipo_elemento = ""
        if(producto == "producto"):
            data = request.form
            if(data["categoria"] == "comida"):
                tipo_elemento = Comidas(nombre = data["nombre"], descripcion = data["descripcion"], imagen = data["imagen"], precio = ["precio"])
            elif(data["categoria"] == "bebidas"):
                tipo_elemento = Bebidas(nombre = data["nombre"], descripcion = data["descripcion"], imagen = data["imagen"], precio = ["precio"])
            elif(data["categoria"] == "tragos"):
                tipo_elemento = Tragos(nombre = data["nombre"], descripcion = data["descripcion"], imagen = data["imagen"], precio = ["precio"])
        db.session.add(tipo_elemento)
        db.session.commit()
    except:
        return {"error" : "errorDeServidor"} , 500



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)