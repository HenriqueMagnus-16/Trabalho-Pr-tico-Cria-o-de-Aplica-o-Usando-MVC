from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    @staticmethod
    def listar():
        return UsuarioRepository.listar()

    @staticmethod
    def criar(dados):

        nome = dados.get("nome")
        email = dados.get("email")
        setor = dados.get("setor")

        if not nome:
            raise ValueError("Nome é obrigatório.")

        if not email:
            raise ValueError("E-mail é obrigatório.")

        if not setor:
            raise ValueError("Setor é obrigatório.")

        if UsuarioRepository.buscar_por_email(email):
            raise ValueError(
                "Já existe um usuário com este e-mail."
            )

        usuario = Usuario(
            nome=nome,
            email=email,
            setor=setor
        )

        return UsuarioRepository.criar(usuario)

    @staticmethod
    def atualizar(usuario_id, dados):

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            raise LookupError("Usuário não encontrado.")

        nome = dados.get("nome")
        email = dados.get("email")
        setor = dados.get("setor")

        if not nome:
            raise ValueError("Nome é obrigatório.")

        if not email:
            raise ValueError("E-mail é obrigatório.")

        if not setor:
            raise ValueError("Setor é obrigatório.")

        outro_usuario = UsuarioRepository.buscar_por_email(email)

        if outro_usuario and outro_usuario.id != usuario.id:
            raise ValueError(
                "Já existe um usuário com este e-mail."
            )

        usuario.nome = nome
        usuario.email = email
        usuario.setor = setor

        return UsuarioRepository.atualizar(usuario)

    @staticmethod
    def excluir(usuario_id):

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            raise LookupError("Usuário não encontrado.")

        if usuario.chamados:
            raise ValueError(
                "Não é possível excluir um usuário "
                "que possui chamados cadastrados."
            )

        UsuarioRepository.excluir(usuario)