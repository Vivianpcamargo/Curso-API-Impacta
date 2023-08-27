from flask import jsonify

database = [{"id": 1, "nome": "Andreia", "media": 8.5},
            {"id": 2, "nome": "Arthur", "media": 10},
            {"id": 3, "nome": "Pedro", "media": 10},
            {"id": 4, "nome": "Ana", "media": 7}]


def get_all():
    if database:
        return jsonify(database)
    return None


def get_aluno_id(id_consulta):
    for aluno in database:
        if aluno['id'] == id_consulta:
            return aluno
    return None


def inserir_aluno(aluno):
    novo_aluno = aluno
    database.append(novo_aluno)
    return


def excluir_aluno(aluno):
    database.remove(aluno)


def alterar_aluno(aluno, novo_aluno):
    excluir_aluno(aluno)
    inserir_aluno(novo_aluno)
    return


def get_aluno_maior_media():
    maior_media = 0
    alunos_maior_media = []
    for aluno in database:
        if aluno['media'] >= maior_media:
            if aluno['media'] > maior_media:
                alunos_maior_media = []
            maior_media = aluno['media']
            alunos_maior_media.append(aluno)

    if alunos_maior_media:
        return jsonify(alunos_maior_media)
    return None
