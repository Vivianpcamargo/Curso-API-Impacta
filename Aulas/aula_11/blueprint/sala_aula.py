from flask import Flask
from alunos_api import alunos_app
from professores_api import professores_app

app = Flask(__name__)

app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
