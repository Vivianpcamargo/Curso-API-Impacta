# aula12_exemplo1.py na versão com flask_ngrok
from flask import Flask, request
from flask_ngrok2 import run_with_ngrok
from pyngrok import ngrok

app = Flask(__name__)

ngrok.set_auth_token("275JW9XPjdA0oXh9lcsl7NiTchd_6S3nK3dU59S8EvQ5MFHQJ")
run_with_ngrok(app)  # inicia ngrok quando app está executando


@app.route('/', methods=['POST'])
def boas_vindas():
    nome = request.get_json(force=True)
    return 'Seja bem-vindo, {}, na aula de Desenvolvimento de APIs e Microsserviços.\n'.format(nome['nome'])


if __name__ == '__main__':
    app.run()
