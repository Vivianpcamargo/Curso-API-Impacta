from flask import Flask, request
from flask import make_response, redirect, render_template
app = Flask(__name__)

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


def autenticar_login():
    login = request.cookies.get("login", "")
    senha = request.cookies.get("senha", "")
    return verificar_login(login, senha)


@app.route("/login")
def form_login():
    logado = autenticar_login()
    if logado is not None:
        return redirect("/dashboard")
    return render_template("login.html", err="")


@app.route("/")
@app.route("/dashboard")
def dashboard():
    logado = autenticar_login()
    if logado is None:
        return redirect("/login")
    return render_template("dashboard.html", user=logado)


@app.route("/login", methods=["POST"])
def fazer_login():
    login = request.form.get("login", "")
    senha = request.form.get("senha", "")
    logado = verificar_login(login, senha)
    if logado is None:
        return render_template("login.html", err="Senha errada"), 302
    resposta = make_response(redirect("/dashboard"))
    resposta.set_cookie("login", login,
                        httponly=True, samesite="Strict")
    resposta.set_cookie("senha", senha,
                        httponly=True, samesite="Strict")
    return resposta


@app.route("/logout", methods=["POST"])
def logout():
    t = render_template("login.html", err="Tchau.")
    resposta = make_response(t)
    resposta.set_cookie("login", "",
                        httponly=True, samesite="Strict")
    resposta.set_cookie("senha", "",
                        httponly=True, samesite="Strict")
    return resposta


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
