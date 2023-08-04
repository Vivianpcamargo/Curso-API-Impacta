from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    'ALUNO': [{"id": 1, "nome": "Andreia"},
              {"id": 2, "nome": "Arthur"},
              {"id": 3, "nome": "Pedro"}],

    'PROFESSOR': [{"id": 1, "nome": "Professor1"},
                  {"id": 2, "nome": "Professor2"},
                  {"id": 3, "nome": "Professor3"}],
}


@app.route('/alunos')
def get_alunos():
    return jsonify(database['ALUNO'])


@app.route('/professores')
def get_profesores():
    return jsonify(database['PROFESSOR'])


@app.route('/show_all')
def get_all():
    return jsonify(database)


@app.route("/")
def start():
    return "Vamos aprender a integrar Requests e Flask!"


@app.route('/alunos', methods=['POST'])
def inserir_aluno():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])


@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localizar_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return 'Aluno não encontrado', 404


@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def excluir_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não encontrado', 404


@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar(id_aluno):
    atualiza_aluno = request.get_json()
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            database['ALUNO'].append(atualiza_aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não encontrado', 404


@app.route('/reseta', methods=['POST'])
def resetar():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return jsonify(database)


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
