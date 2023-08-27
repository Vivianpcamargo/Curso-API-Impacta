from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def boas_vindas():
    nome = request.get_json(force=True)
    return 'Seja bem-vindo, {}, na aula de Desevolvimento de APIs e Microsserviços.\n'.format(nome['nome'])


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
