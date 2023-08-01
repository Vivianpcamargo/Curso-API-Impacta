from flask import Flask, request, session
from flask import redirect, render_template
app = Flask(__name__)

app.secret_key = "Grande segredo secreto e misterioso"

usuarios = [
    {"login": "Maria", "senha": "1234"},
    {"login": "Roberto", "senha": "4321"},
    {"login": "Carlos", "senha": "abcd"},
    {"login": "Paula", "senha": "xyz"}
]


def verificar_login(login, senha):
    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            return u
    return None


@app.route("/login")
def form_login():
    if "logado" in session:
        return redirect("/dashboard")
    return render_template("login.html", err="")


@app.route("/")
@app.route("/dashboard")
def dashboard():
    if "logado" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["logado"])


@app.route("/login", methods=["POST"])
def fazer_login():
    login = request.form.get("login", "")
    senha = request.form.get("senha", "")
    logado = verificar_login(login, senha)
    if logado is None:
        return render_template("login.html", err="Senha errada"), 302
    session["logado"] = logado
    return redirect("/dashboard")


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("logado", None)
    return render_template("login.html", err="Tchau.")


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
