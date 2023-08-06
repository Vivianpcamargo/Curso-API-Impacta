import model.aluno_model as aluno_model


# listar todos os alunos do database
def listar():
    alunos = aluno_model.get_all()
    if alunos is None:
        return 'Não existem alunos cadastrados. Verifique!'
    return alunos


def localiza_por_id(id_consulta):
    aluno = aluno_model.get_aluno_id(id_consulta)
    if aluno is None:
        return 'Aluno não encontrado'
    return {"Status": "Aluno encontrado", "Aluno": aluno}


def localizar_por_maior_media():
    alunos = aluno_model.get_aluno_maior_media()
    return alunos


def inserir_aluno(aluno):
    aluno_model.inserir_aluno(aluno)
    return listar()


def excluir_por_id(id_deletar):
    aluno = aluno_model.get_aluno_id(id_deletar)
    if aluno is None:
        return 'Aluno não encontrado'

    aluno_model.excluir_aluno(aluno)
    return listar()


def alterar_aluno(id_alterar, novo_aluno):
    aluno = aluno_model.get_aluno_id(id_alterar)
    if aluno is None:
        return 'Aluno não encontrado'

    aluno_model.alterar_aluno(aluno, novo_aluno)
    return listar()


'''
def localizar(id):
    aluno = dao_consultar(id)
    if aluno == None:
        return None
    return aluno.__dict__()
'''
