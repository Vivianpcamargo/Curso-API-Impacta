from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/bom-dia")
@app.route("/good-morning")
def bom_dia():
    return 'Bom dia'


@app.route("/boa-tarde")
def boa_tarde():
    return 'Boa tarde'


@app.route("/boa-noite")
def boa_noite():
    return 'Boa noite'


@app.route("/um/caminho/com/varios/elementos")
def um_caminho_longo():
    return "Oi, pessoal!"


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
