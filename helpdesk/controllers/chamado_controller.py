from flask import Blueprint, request, jsonify
from services.chamado_service import ChamadoService


chamado_controller = Blueprint(
    "chamado_controller",
    __name__
)


def chamado_json(chamado):

    return {
        "id": chamado.id,
        "titulo": chamado.titulo,
        "descricao": chamado.descricao,
        "prioridade": chamado.prioridade,
        "status": chamado.status,
        "tecnico": chamado.tecnico,
        "data_abertura": chamado.data_abertura.isoformat(),
        "usuario_id": chamado.usuario_id
    }


@chamado_controller.route(
    "/usuarios/<int:id>/chamados",
    methods=["GET"]
)
def listar_chamados_usuario(id):

    try:

        chamados = ChamadoService.listar_por_usuario(id)

        return jsonify([
            chamado_json(chamado)
            for chamado in chamados
        ]), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404


@chamado_controller.route(
    "/chamados",
    methods=["GET"]
)
def listar_chamados():

    chamados = ChamadoService.listar()

    return jsonify([
        chamado_json(chamado)
        for chamado in chamados
    ]), 200


@chamado_controller.route(
    "/chamados",
    methods=["POST"]
)
def criar_chamado():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "JSON não informado."
        }), 400

    try:

        chamado = ChamadoService.criar(dados)

        return jsonify(
            chamado_json(chamado)
        ), 201

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400


@chamado_controller.route(
    "/chamados/<int:id>",
    methods=["PUT"]
)
def atualizar_chamado(id):

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "JSON não informado."
        }), 400

    try:

        chamado = ChamadoService.atualizar(
            id,
            dados
        )

        return jsonify(
            chamado_json(chamado)
        ), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400


@chamado_controller.route(
    "/chamados/<int:id>",
    methods=["DELETE"]
)
def excluir_chamado(id):

    try:

        ChamadoService.excluir(id)

        return jsonify({
            "mensagem": "Chamado excluído com sucesso."
        }), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404


@chamado_controller.route(
    "/chamados/<int:id>/iniciar",
    methods=["PATCH"]
)
def iniciar_chamado(id):

    try:

        chamado = ChamadoService.iniciar(id)

        return jsonify(
            chamado_json(chamado)
        ), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400


@chamado_controller.route(
    "/chamados/<int:id>/encerrar",
    methods=["PATCH"]
)
def encerrar_chamado(id):

    try:

        chamado = ChamadoService.encerrar(id)

        return jsonify(
            chamado_json(chamado)
        ), 200

    except LookupError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400


@chamado_controller.route(
    "/chamados/abertos",
    methods=["GET"]
)
def chamados_abertos():

    chamados = ChamadoService.listar_abertos()

    return jsonify([
        chamado_json(chamado)
        for chamado in chamados
    ]), 200


@chamado_controller.route(
    "/chamados/prioridade/alta",
    methods=["GET"]
)
def chamados_prioridade_alta():

    chamados = ChamadoService.listar_prioridade_alta()

    return jsonify([
        chamado_json(chamado)
        for chamado in chamados
    ]), 200


@chamado_controller.route(
    "/estatisticas",
    methods=["GET"]
)
def estatisticas():

    return jsonify(
        ChamadoService.estatisticas()
    ), 200