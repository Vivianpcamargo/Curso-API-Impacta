from flask import Flask, request
app = Flask(__name__)


@app.route("/exemplo1")
def exemplo1():
    pagina = request.args["pg"]
    return f"O valor lido foi {pagina}."


@app.route("/exemplo2")
def exemplo2():
    pagina = request.args.get("pg")
    return f"O valor lido foi {pagina}."


@app.route("/exemplo3")
def exemplo3():
    pagina = request.args.get("pg", "vazio")
    return f"O valor lido foi {pagina}."


@app.route("/exemplo4")
def exemplo4():
    pagina = request.args.getlist("pg")
    return f"O valor lido foi {pagina}."


if __name__ == "__main__":
    app.run(host="localhost", port=5002)
