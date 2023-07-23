from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///autentica.db')


def criar_tabelas():
    with engine.connect() as con:
        create_tabela_senhas = """
        CREATE TABLE IF NOT EXISTS users (
            login TEXT NOT NULL,
            senha TEXT NOT NULL
        )
        """
        con.execute(create_tabela_senhas)


def criar_usuarios():
    with engine.connect() as con:
        add_usuaria = "INSERT INTO users (login, senha) VALUES ('Minerva','123')"
        con.execute(add_usuaria)
        add_usuario = "INSERT INTO users (login, senha) VALUES ('José','Carabina')"
        con.execute(add_usuario)
        add_admin = "INSERT INTO users (login, senha) VALUES ('admin','eLl96BFLVsoPrcOJGa0PhvwFnxt7ThKn')"
        con.execute(add_admin)


def validar_admin(senha):
    with engine.connect() as con:
        sql_admin = text(
            f"SELECT * FROM users WHERE login='admin' and senha='{senha}'")
        print(sql_admin)
        rs = con.execute(sql_admin)
        result = rs.fetchone()
        if result == None:
            return 'nao autorizado'
        return 'autorizado'

# ataque malicioso
    # validar_admin("nao sei' OR 'a'='a")


def validar_seguro(senha):
    with engine.connect() as con:
        sql_admin = text(
            "SELECT * FROM users WHERE login='admin' and senha= :senha")
        print(sql_admin)
        rs = con.execute(sql_admin, senha=senha)
        result = rs.fetchone()
        if result == None:
            return 'nao autorizado'
        return 'autorizado'

# sql injection
    # sql injection é uma vulnerabilidade de segurança que ocorre quando
    # usamos input do usuário para montar a string SQL a ser executada

# prepared statement
    # prepared statement é a proteção contra sql injection
    # criamos strings sql que informam à nossa biblioteca de acesso
    # ao banco de dados qual parte da string é codificada por nós
    # e qual parte é input do usuário
    # no nosso caso, a sintaxe para prepared statement é como no exemplo:
    # sql_admin = text ("SELECT * FROM users WHERE login='admin' and senha= :senha")
    # rs = con.execute(sql_admin , senha=senha)
