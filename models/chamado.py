from database import db
from datetime import datetime


class Chamado(db.Model):
    __tablename__ = "chamados"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="Aberto")
    tecnico = db.Column(db.String(100), nullable=True)

    data_abertura = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="chamados"
    )