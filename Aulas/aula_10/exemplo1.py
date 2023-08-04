from flask import Flask

app = Flask(__name__)


@app.route("/")
def start():
    return "Vamos aprender a integrar Requests e Flask!"


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
