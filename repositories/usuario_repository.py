from database import db
from models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def listar():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(usuario_id):
        return db.session.get(Usuario, usuario_id)

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def criar(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def atualizar(usuario):
        db.session.commit()
        return usuario

    @staticmethod
    def excluir(usuario):
        db.session.delete(usuario)
        db.session.commit()