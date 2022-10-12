
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///biblioteca.db')

# mas se quisesse uma solução mais robusta, poderia
# usar mudando o código muito pouco
# engine = create_engine('postgresql://usuario:senha@localhost:5432/imobiliaria')


# criar a tabela
def criar_tabelas():
    with engine.connect() as con:
        create_tabela_aluno = """
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
        rs = con.execute(create_tabela_aluno)
        create_tabela_livro = """
        CREATE TABLE IF NOT EXISTS Livro (
            id_livro INTEGER PRIMARY KEY,
            id_aluno INTEGER,
            descricao TEXT NOT NULL,
            FOREIGN KEY(id_aluno) REFERENCES Aluno(id)  
        )
        """
        rs = con.execute(create_tabela_livro)

def criar_alunos():
    with engine.connect() as con:
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com');"
        rs = con.execute(add_aluno)

def criar_livros():
    with engine.connect() as con:
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1,1,'Python completo e total')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias póstumas de brás cubas')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')"
        rs = con.execute(add_livro)

# criar_tabelas()
# criar_alunos()

class AlunoNaoExisteException(Exception):
    pass
# estamos definindo uma classe AlunoNaoExisteException, que
# herda todas as funcionalidades, todos os métodos e atributos,
# de Exception
# no lugar do pass, escreveríamos as mudanças,
# as coisas que AlunoNaoExisteException faz diferente de Exception
# mas não fizemos mudança nenhuma (por isso pass)




# 1) Crie uma função consulta_aluno que recebe a id de um aluno e devolve um dicionário com os dados desse aluno

# R:
def consulta_aluno(id_aluno):
    with engine.connect() as con:   # conectar ao banco de dados 
        sql_consulta = text ("SELECT * FROM aluno WHERE id = :id_do_aluno")
        # id          : nome da coluna da tabela
        # id_aluno    : nome da variavel python que a funcao recebeu
        # id_do_aluno : nome do "buraco" definido na query sql_consulta
        #               nome passado como argumento do con.execute
        rs = con.execute(sql_consulta, id_do_aluno = id_aluno)
        # executamos a query definida em sql_consulta, preenchendo o "buraco" :id_do_aluno
        result = rs.fetchone()
        # fetchone: pega uma linha do resultado
        # se tiver mais linhas, podemos pegar a próxima com outro fetchone
        # se não tiver mais linhas, receberemos um None
        if result == None: #se a query retornou 0 linhas, o primeiro fetchone já resulta None
            raise AlunoNaoExisteException
        # As linhas que o sqlalchemy devolve são parecidas com dicionários,
        # mas não é exatamente a mesma coisa. Por isso, fazemos uma conversão
        return dict(result)

# 1b) Crie uma função todos_alunos que retorna um lista com um dicionario para cada aluno

# R:
def todos_aluno():
    with engine.connect() as con:
        sql_consulta = text ("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados = []
        while True: # que roda pra sempre
            result = rs.fetchone()
            if result == None: # se a query retornou 0 linhas, o primeiro fetchone já resulta None
                break
            d_result = dict(result)
            resultados.append(d_result)
        return resultados

# 1c) Crie uma função todos_livros que retorna um lista com um dicionario para cada livro

# R:
def todos_livros():
    with engine.connect() as con:
        sql_consulta = text ("SELECT * FROM livro")
        rs = con.execute(sql_consulta)
        resultados = []
        while True: # que roda pra sempre
            result = rs.fetchone()
            if result == None: # se a query retornou 0 linhas, o primeiro fetchone já resulta None
                break
            d_result = dict(result)
            resultados.append(d_result)
        return resultados

# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição) e o adiciona no banco de dados

# R:
def cria_livro(id_livro, descricao):
    with engine.connect() as con:
        sql_create = text ("INSERT INTO (id_livro, descricao) VALUES (:id_livro, :descricao)")
        con.execute(sql_create, id_livro = id_livro, descricao = descricao)

# 3) Crie uma função empresta_livro, que recebe a id de um livro, a id de um aluno e marca o livro como emprestado pelo aluno

# R:
def empresta_livro(id_aluno, id_livro):
    with engine.connect() as con:
        sql_update = text ("UPDATE livro SET id_aluno = :id_aluno WHERE id_livro = :id_livro")
        con.execute(sql_update, id_aluno = id_aluno, id_livro = id_livro)

# 4) Crie uma função devolve_livro, que recebe a id de um livro, e marca o livro como disponível

# R:
def devolve_livro(id_livro):
    with engine.connect() as con:
        sql_update = text ("UPDATE livro SET id_aluno = NULL WHERE id_livro = :id_livro")
        con.execute(sql_update, id_livro = id_livro)
# NULL é o valor "vazio" ou "inválido" do SQL
# NULL é o valor "vazio" ou "inválido" do Python
# NULL na tabela vira None no dicionário

# 5) Crie uma função livros_parados que devolve a lista de todos os livros que não estão emprestados por ninguém (uma lista de dicionários, um para cada livro)

# R:
def livros_parados():
    with engine.connect() as con:
        sql_consulta = text ("SELECT * FROM livro WHERE id_aluno ISNULL")
        rs = con.execute(sql_consulta)
        resultados = []
        while True: # que roda pra sempre
            result = rs.fetchone()
            if result == None: # se a query retornou 0 linhas, o primeiro fetchone já resulta None
                break
            d_result = dict(result)
            resultados.append(d_result)
        return resultados

# 6) Crie uma função livros_do_aluno, recebe o nome do aluno e devolve a lista de todos os livros que estão com o aluno no momento

# R:
def livros_do_aluno(nome):
    with engine.connect() as con:
        sql_consulta = text ("SELECT id_livro, id_aluno, descricao FROM livro JOIN aluno ON livro.id_aluno = aluno.id WHERE aluno.nome = :nome")
        rs = con.execute(sql_consulta, nome = nome)
        resultados = []
        while True: # que roda pra sempre
            result = rs.fetchone()
            if result == None: # se a query retornou 0 linhas, o primeiro fetchone já resulta None
                break
            d_result = dict(result)
            resultados.append(d_result)
        return resultados