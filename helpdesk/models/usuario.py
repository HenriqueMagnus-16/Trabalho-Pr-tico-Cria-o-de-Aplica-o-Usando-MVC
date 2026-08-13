from database import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    setor = db.Column(db.String(100), nullable=False)

    chamados = db.relationship(
        "Chamado",
        back_populates="usuario"
    )