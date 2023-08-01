from flask import Flask, redirect, render_template, request
app = Flask(__name__)

frutas = [
    {"nome": "uva", "cor": "roxa"},
    {"nome": "maçã", "cor": "vermelha"},
    {"nome": "morango", "cor": "vermelha"}
]


@app.route("/frutas")
def listar_frutas():
    return render_template("listar_frutas.html", listagem=frutas)


@app.route("/frutas/novo")
def form_criar_frutas():
    return render_template("cadastrar_fruta.html")


@app.route("/frutas", methods=["POST"])
def criar_fruta():
    f = request.form
    frutas.append({"nome": f["nome"], "cor": f["cor"]})
    return redirect("/frutas")


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
