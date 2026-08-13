from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService


usuario_controller = Blueprint(
    "usuario_controller",
    __name__
)


def usuario_json(usuario):

    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "setor": usuario.setor
    }


@usuario_controller.route("/usuarios", methods=["GET"])
def listar_usuarios():

    usuarios = UsuarioService.listar()

    return jsonify([
        usuario_json(usuario)
        for usuario in usuarios
    ]), 200


@usuario_controller.route("/usuarios", methods=["POST"])
def criar_usuario():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "JSON não informado."
        }), 400

    try:

        usuario = UsuarioService.criar(dados)

        return jsonify(
            usuario_json(usuario)
        ), 201

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400


@usuario_controller.route(
    "/usuarios/<int:id>",
    methods=["PUT"]
)
def atualizar_usuario(id):

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "JSON não informado."
        }), 400

    try:

        usuario = UsuarioService.atualizar(
            id,
            dados
        )

        return jsonify(
            usuario_json(usuario)
        ), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400


@usuario_controller.route(
    "/usuarios/<int:id>",
    methods=["DELETE"]
)
def excluir_usuario(id):

    try:

        UsuarioService.excluir(id)

        return jsonify({
            "mensagem": "Usuário excluído com sucesso."
        }), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400