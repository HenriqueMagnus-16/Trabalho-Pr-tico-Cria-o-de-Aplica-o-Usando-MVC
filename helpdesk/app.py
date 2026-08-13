from flask import Flask, jsonify

from database import db

from controllers.usuario_controller import usuario_controller
from controllers.chamado_controller import chamado_controller

from models.usuario import Usuario
from models.chamado import Chamado


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(usuario_controller)
app.register_blueprint(chamado_controller)


with app.app_context():
    db.create_all()


@app.route("/")
def inicio():

    return jsonify({
        "mensagem": "API Helpdesk funcionando!"
    })


if __name__ == "__main__":
    app.run(debug=True)