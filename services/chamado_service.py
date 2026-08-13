from models.chamado import Chamado
from repositories.chamado_repository import ChamadoRepository
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime


class ChamadoService:

    PRIORIDADES = ["Baixa", "Média", "Alta"]

    STATUS_ABERTO = "Aberto"
    STATUS_ATENDIMENTO = "Em atendimento"
    STATUS_ENCERRADO = "Encerrado"

    @staticmethod
    def listar():
        return ChamadoRepository.listar()

    @staticmethod
    def listar_por_usuario(usuario_id):

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            raise LookupError("Usuário não encontrado.")

        return ChamadoRepository.listar_por_usuario(usuario_id)

    @staticmethod
    def criar(dados):

        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        prioridade = dados.get("prioridade")
        tecnico = dados.get("tecnico")
        usuario_id = dados.get("usuario_id")

        if not titulo:
            raise ValueError("Título é obrigatório.")

        if len(titulo) < 5:
            raise ValueError(
                "O título deve possuir pelo menos 5 caracteres."
            )

        if not descricao:
            raise ValueError("Descrição é obrigatória.")

        if len(descricao) < 10:
            raise ValueError(
                "A descrição deve possuir pelo menos 10 caracteres."
            )

        if prioridade not in ChamadoService.PRIORIDADES:
            raise ValueError(
                "Prioridade deve ser Baixa, Média ou Alta."
            )

        if not usuario_id:
            raise ValueError(
                "O chamado deve obrigatoriamente "
                "estar vinculado a um usuário."
            )

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            raise LookupError("Usuário não encontrado.")

        quantidade = ChamadoRepository.contar_pendentes_usuario(
            usuario_id
        )

        if quantidade >= 5:
            raise ValueError(
                "O usuário já possui cinco chamados "
                "não encerrados."
            )

        chamado = Chamado(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            status=ChamadoService.STATUS_ABERTO,
            tecnico=tecnico,
            data_abertura=datetime.utcnow(),
            usuario_id=usuario_id
        )

        return ChamadoRepository.criar(chamado)

    @staticmethod
    def atualizar(chamado_id, dados):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            raise LookupError("Chamado não encontrado.")

        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        prioridade = dados.get("prioridade")
        tecnico = dados.get("tecnico")
        usuario_id = dados.get("usuario_id")

        if not titulo:
            raise ValueError("Título é obrigatório.")

        if len(titulo) < 5:
            raise ValueError(
                "O título deve possuir pelo menos 5 caracteres."
            )

        if not descricao:
            raise ValueError("Descrição é obrigatória.")

        if len(descricao) < 10:
            raise ValueError(
                "A descrição deve possuir pelo menos 10 caracteres."
            )

        if prioridade not in ChamadoService.PRIORIDADES:
            raise ValueError(
                "Prioridade deve ser Baixa, Média ou Alta."
            )

        if not usuario_id:
            raise ValueError(
                "O chamado deve estar vinculado a um usuário."
            )

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            raise LookupError("Usuário não encontrado.")

        chamado.titulo = titulo
        chamado.descricao = descricao
        chamado.prioridade = prioridade
        chamado.tecnico = tecnico
        chamado.usuario_id = usuario_id

        return ChamadoRepository.atualizar(chamado)

    @staticmethod
    def excluir(chamado_id):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            raise LookupError("Chamado não encontrado.")

        ChamadoRepository.excluir(chamado)

    @staticmethod
    def iniciar(chamado_id):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            raise LookupError("Chamado não encontrado.")

        if chamado.status != ChamadoService.STATUS_ABERTO:
            raise ValueError(
                "Somente chamados abertos podem "
                "ser colocados em atendimento."
            )

        chamado.status = ChamadoService.STATUS_ATENDIMENTO

        return ChamadoRepository.atualizar(chamado)

    @staticmethod
    def encerrar(chamado_id):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            raise LookupError("Chamado não encontrado.")

        if chamado.status != ChamadoService.STATUS_ATENDIMENTO:
            raise ValueError(
                "Somente chamados em atendimento "
                "podem ser encerrados."
            )

        chamado.status = ChamadoService.STATUS_ENCERRADO

        return ChamadoRepository.atualizar(chamado)

    @staticmethod
    def listar_abertos():
        return ChamadoRepository.listar_abertos()

    @staticmethod
    def listar_prioridade_alta():
        return ChamadoRepository.listar_prioridade_alta()

    @staticmethod
    def estatisticas():

        usuarios = UsuarioRepository.listar()

        return {
            "usuarios": len(usuarios),
            "chamados": ChamadoRepository.contar_total(),
            "abertos": ChamadoRepository.contar_por_status(
                "Aberto"
            ),
            "em_atendimento": ChamadoRepository.contar_por_status(
                "Em atendimento"
            ),
            "encerrados": ChamadoRepository.contar_por_status(
                "Encerrado"
            )
        }