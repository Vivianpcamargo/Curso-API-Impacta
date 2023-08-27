from flask import Flask, request
from flask_ngrok2 import run_with_ngrok
from pyngrok import ngrok

import controller.aluno_controller as aluno_controller

app = Flask(__name__)
ngrok.set_auth_token("275JW9XPjdA0oXh9lcsl7NiTchd_6S3nK3dU59S8EvQ5MFHQJ")
run_with_ngrok(app)  # inicia ngrok quando app está executando


@app.route('/alunos')
def get_alunos():
    return aluno_controller.listar()


@app.route("/alunos/<int:id_consulta>", methods=["GET"])
def get_aluno_id(id_consulta):
    return aluno_controller.localiza_por_id(id_consulta)


@app.route("/alunos/maior_media", methods=["GET"])
def get_alunos_maior_media():
    return aluno_controller.localizar_por_maior_media()


@app.route("/alunos", methods=["POST"])
def inserir():
    aluno = request.get_json(force=True)
    return aluno_controller.inserir_aluno(aluno)


@app.route("/alunos/<int:id_deletar>", methods=["DELETE"])
def excluir(id_deletar):
    return aluno_controller.excluir_por_id(id_deletar)


@app.route("/alunos/<int:id_alterar>", methods=["PUT"])
def alterar(id_alterar):
    aluno = request.get_json(force=True)
    return aluno_controller.alterar_aluno(id_alterar, aluno)


@app.route('/')
def start():
    return "Construindo nossa aplicação com MVC"


if __name__ == '__main__':
    app.run()
