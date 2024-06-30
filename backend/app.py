from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Comidas, Bebidas, Tragos, Combos


app = Flask(__name__)
CORS(app)
port=5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://matias:matias@localhost:5432/tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route("/")
def home():
    comidas = Comidas.query.all()
    
    info_comidas = []
    info_de_comida = {
        "id_comida" : 1,
        "nombre" : "comida.nombre",
        "descripcion" : "comida.descripcion",
        "imagen" : "comida.imagen",
        "precio" : 10
    }
    info_comidas.append(info_de_comida)
    
    
    
    return jsonify(info_comidas)


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)