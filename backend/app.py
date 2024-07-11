from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Comidas, Bebidas, Tragos, Combos

app = Flask(__name__)
CORS(app)
port=5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://tp:tp@localhost:5432/tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

NO_SELECCIONADO = -1


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
            data_producto = request.form
            if(data_producto["categoria"] == "comida"):
                tipo_elemento = Comidas(nombre = data_producto["nombre"], descripcion = data_producto["descripcion"], imagen = data_producto["imagen"], precio = data_producto["precio"])
            elif(data_producto["categoria"] == "bebidas"):
                tipo_elemento = Bebidas(nombre = data_producto["nombre"], descripcion = data_producto["descripcion"], imagen = data_producto["imagen"], precio = data_producto["precio"])
            elif(data_producto["categoria"] == "tragos"):
                tipo_elemento = Tragos(nombre = data_producto["nombre"], descripcion = data_producto["descripcion"], imagen = data_producto["imagen"], precio = data_producto["precio"])
            elemento_creado = {
                "nombre" : data_producto["nombre"],
                "descripcion" : data_producto["descripcion"],
                "imagen" : data_producto["imagen"],
                "precio" : data_producto["precio"]
            }
        elif(producto == "combo"):
            data_combo = request.form
            comida_seleccionada = Comidas.query.get(data_combo["comidas"])
            bebida_seleccionada = Bebidas.query.get(data_combo["bebidas"])
            trago_seleccionado = Tragos.query.get(data_combo["tragos"])
            elemento_creado = {
                "nombre" : data_combo["nombre"],
                "descripcion" : comida_seleccionada.descripcion + ", " + bebida_seleccionada.descripcion + " y " + trago_seleccionado.descripcion,
                "imagen" : data_combo["imagen"],
                "precio" : comida_seleccionada.precio + bebida_seleccionada.precio + trago_seleccionado.precio,
                "id_comida" : data_combo["comidas"],
                "id_bebida" : data_combo["bebidas"],
                "id_trago" : data_combo["tragos"]
            }
            tipo_elemento = Combos(nombre = elemento_creado["nombre"], descripcion = elemento_creado["descripcion"], imagen = elemento_creado["imagen"], precio = elemento_creado["precio"], id_comida = data_combo["comidas"], id_bebida = data_combo["bebidas"], id_tragos = data_combo["tragos"])
        
        db.session.add(tipo_elemento)
        db.session.commit()
        
        return f"creado {jsonify(elemento_creado)}"
    except:
        return {"error" : "errorDeServidor"} , 500
"""
@app.route("/modificar", methods = ["DELETE", "PUT", "GET"])
def procesar_request():
    try:
        if (request.method == "DELETE"):
            argumentos = request.args.to_dict()
            if(argumentos.get("tipo") == "comidas"):
                elemento = Comidas.query.filter_by(id = argumentos.get("id")).delete()
            elif(argumentos.get("tipo") == "bebidas"):
                elemento = Bebidas.query.filter_by(id = argumentos.get("id")).delete()
            elif(argumentos.get("tipo") == "tragos"):
                elemento = Tragos.query.filter_by(id = argumentos.get("id")).delete()
            elif(argumentos.get("tipo") == "combos"):
                elemento = Combos.query.filter_by(id = argumentos.get("id")).delete()
            db.session.commit()
            return f"eliminado {jsonify(elemento)}"
    except:
       return {"error" : "errorDeServidorAlEliminarElemento"} , 500 
"""   




if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)