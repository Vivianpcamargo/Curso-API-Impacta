from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/uma-lista")
def uma_lista():
    return jsonify([0, 1, 2, 3])


@app.route("/bom-dia")
def bom_dia():
    return jsonify("Bom dia")


@app.route("/numero-da-sorte")
def numero_da_sorte():
    return jsonify(42)


@app.route("/nada-a-dizer")
def nada():
    return jsonify(None)


@app.route("/sim")
def sim():
    return jsonify(True)


@app.route("/nao")
def nao():
    return jsonify(False)


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
