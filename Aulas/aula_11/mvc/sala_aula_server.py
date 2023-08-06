from flask import Flask, request

import controller.aluno_controller as aluno_controller

app = Flask(__name__)


@app.route('/alunos')
def get_alunos():
    return aluno_controller.listar()


@app.route("/alunos/<int:id_consulta>", methods=["GET"])
def get_aluno_id(id_consulta):
    return aluno_controller.localiza_por_id(id_consulta)


@app.route("/alunos/maior_media", methods=["GET"])
def get_aluno_maior_media():
    return aluno_controller.localizar_por_maior_media()


@app.route("/alunos", methods=["POST"])
def inserir():
    aluno = request.json
    return aluno_controller.inserir_aluno(aluno)


@app.route("/alunos/<int:id_deletar>", methods=["DELETE"])
def excluir(id_deletar):
    return aluno_controller.excluir_por_id(id_deletar)


@app.route("/alunos/<int:id_alterar>", methods=["PUT"])
def alterar(id_alterar):
    aluno = request.json
    return aluno_controller.alterar_aluno(id_alterar, aluno)


@app.route('/')
def start():
    return "Construindo nossa aplicação com MVC"


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
