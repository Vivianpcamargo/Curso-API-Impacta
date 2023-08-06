from flask import jsonify, Blueprint

alunos_app = Blueprint('alunos_app', __name__,
                       template_folder='templates')


database = {
    'ALUNO': [{"id": 1, "nome": "Andreia"},
              {"id": 2, "nome": "Arthur"},
              {"id": 3, "nome": "Pedro"}]
}

# rota /alunos padrão GET: retorna todos os alunos


@alunos_app.route('/alunos')
def get_alunos():
    return jsonify(database['ALUNO'])
