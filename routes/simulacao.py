from flask import Blueprint, render_template

pesquisador_route = Blueprint('pesquisador',__name__)

"""
Rotas de Pesquisadores

	-/pesquisador/ (GET) - Listar os pesquisadores
	-/pesquisador/ (POST) - Inserir o pesquisador no servidor
	-/pesquisador/new (GET) - Formulario para criar um pesquisador
	-/pesquisador/<id> (GET) - Obter os dados de um pesquisador
	-/pesquisador/<id>/edit (GET) - Formulario para editar um pesquisador
	-/pesquisador/<id>/update (PUT) - Atualizar os dados do pesquisador
	-/pesquisador/<id>/delete - Deleta o registro do usuario

	-/simulacao/ - Listar todas simulacoes atuais
	-/simulacao/<id> Obter os dados da simulacao selecionada

"""

