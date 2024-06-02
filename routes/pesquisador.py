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
"""


@pesquisador_route.route('/')
def lista_pesquisador():
	# Listar todos os pesquisadores
	return render_template('lista_pesquisador.hmtl')

@pesquisador_route.route('/', methods=['POST'])
def inserir_pesquisador():
	# Inserir os dados do pesquisador no banco de dados
	pass

@pesquisador_route.route('/new')
def form_cadastrar_pesquisador():
	# Formulario para cadastrar um pesquisador
	return render_template('form_cadastrar_pesquisador.hmtl')

@pesquisador_route.route('/<int:pesquisador_id>', methods=['GET'])
def detalhe_pesquisador(pesquisador_id):
	# Obter os dados de um pesquisador
	pass

@pesquisador_route.route('/<int:pesquisador_id>/edit', methods=['GET'])
def form_editar_pesquisador(pesquisador_id):
	# Formulario para editar um pesquisador
	pass

@pesquisador_route.route('/<int:pesquisador_id>/update', methods=['PUT'])
def atualizar_pesquisador(pesquisador_id):
	# Deletar dados de pesquisador
	pass

@pesquisador_route.route('/<int:pesquisador_id>/delete', methods=['DELETE'])
def deletar_pesquisador(pesquisador_id):
	# Deletar dados de pesquisador
	pass