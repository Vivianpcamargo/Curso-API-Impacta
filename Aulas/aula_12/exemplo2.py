from flask import Flask
from flask_ngrok2 import run_with_ngrok
from pyngrok import ngrok

app = Flask(__name__)

ngrok.set_auth_token("275JW9XPjdA0oXh9lcsl7NiTchd_6S3nK3dU59S8EvQ5MFHQJ")
run_with_ngrok(app)


@app.route('/')
def start():
    return 'Seja bem-vindo na aula de Desenvolvimento de APIs e Microsserviços.'


if __name__ == '__main__':
    app.run()
