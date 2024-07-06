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
        informacion_de_comidas = []
        for comida in comidas:
            info_comida = {
                "id" : comida.id,
                "nombre" : comida.nombre,
                "descripcion" : comida.descripcion,
                "imagen" : comida.imagen,
                "precio" : comida.precio
            }
            informacion_de_comidas.append(info_comida)
        informacion_de_bebidas = []
        for bebida in bebidas:
            info_bebida = {
                "id" : bebida.id,
                "nombre" : bebida.nombre,
                "descripcion" : bebida.descripcion,
                "imagen" : bebida.imagen,
                "precio" : bebida.precio
            }
            informacion_de_bebidas.append(info_bebida)
        informacion_de_tragos = []
        for trago in tragos:
            info_trago = {
                "id" : trago.id,
                "nombre" : trago.nombre,
                "descripcion" : trago.descripcion,
                "imagen" : trago.imagen,
                "precio" : trago.precio
            }
            informacion_de_tragos.append(info_trago)
        
        informacion_de_productos = {
            "comidas" : informacion_de_comidas,
            "bebidas" : informacion_de_bebidas,
            "tragos" : informacion_de_tragos,
            "combos" : informacion_de_combos
        }
        return jsonify(informacion_de_productos)
    except:
        return {"error" : "errorDeServidor0"} , 500

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
        return jsonify(tipo_elemento)
    except:
        return {"error" : "errorDeServidor"} , 500
"""
@app.route("modificar", methods = ["DELETE", "PUT", "GET"])
def procesar_request():
    tipo_contenido = request.headers.get('Content-Type')
    if (tipo_contenido == 'application/json'):
        request = request.json
        if(request["modificacion"] == "borrar"):
            if(request["tipo_elemento"] == "comida"):

    else:
        return 'Content-Type not supported!'
"""    



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)