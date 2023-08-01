from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/bom-dia")
def bom_dia():
    return render_template("oi.html", mensagem="Bom dia")


@app.route("/boa-tarde")
def boa_tarde():
    return render_template("oi.html", mensagem="Boa tarde")


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
