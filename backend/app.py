from flask import Flask
from flask_cors import CORS
from models import db, Comidas, Bebidas, Tragos, Combos


app = Flask(__name__)
CORS(app)
port=5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://matias:matias@localhost:5432/tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route("/")
def home():
    return "Night Club"


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)