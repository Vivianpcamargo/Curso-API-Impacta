from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///biblioteca.db')

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
            FOREIGN KEY(id_aluno) REFERENCES Aluno(id)  -- essa constraint é uma boa,
                                                        -- mas o SQLite está ignorando
                                                        -- em bancos mais sofisticados,
                                                        -- (como MySQL e Postgres)
                                                        -- ela impede que haja livro
                                                        -- com id_aluno invalida
                                                        -- id_aluno pode ser null,
                                                        -- mas se tiver algum valor,
                                                        -- tem que ser válido
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

# podemos executar a função criar livros várias vezes?
    # nao, ocasiona um erro, por violar a constraint de unicidade

# podemos executar a função criar tabelas várias vezes?
    # sim, porque o comando usado é create table SE ELA NAO EXISTIR

def todos_alunos():
    with engine.connect() as con:
        sql_consulta = text ("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados = []
        while True:
            result = rs.fetchone()
            if result == None:
                break
            d_result = dict(result)
            resultados.append(d_result)
        return resultados


def todos_alunos_versao2():
    with engine.connect() as con:
        sql_consulta = text ("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados_sujo = rs.fetchall()
        resultados_limpo = []
        for resultado in resultados_sujo:
            resultados_limpo.append(dict(resultado))
        return resultados_limpo

# fetchone, fetchmany(20), fetchall
  # pegam, respectivamente, uma linha do resultado
  #                         vinte linhas do resultado
  #                         todas as linhas do resultado
  # fetchone pode ser ineficiente por fazer muitos acessos ao disco rigido
  #           (pois o disco rígido é muito mais lento que a RAM, onde ficam as variáveis normais)
  # fetchall pode ser ineficiente por carregar dados demais para a RAM,
  #            impedindo o servidor de processar outras demandas

def todos_alunos_versao3():
    with engine.connect() as con:
        sql_consulta = text ("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados_limpo = []
        while True:
            resultados_sujo = rs.fetchmany(20)
            if resultados_sujo == []:
                break
            for resultado in resultados_sujo:
                resultados_limpo.append(dict(resultado))
        return resultados_limpo
