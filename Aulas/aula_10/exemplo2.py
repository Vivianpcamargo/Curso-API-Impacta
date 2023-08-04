from flask import Flask, jsonify

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


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
