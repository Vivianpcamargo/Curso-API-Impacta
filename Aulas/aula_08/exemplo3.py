from flask import Flask, request, jsonify

app = Flask(__name__)

pessoas = [
    {"nome": "Paulo", "sexo": "M", "cabelo": "loiro"},
    {"nome": "Maria", "sexo": "F", "cabelo": "preto"},
    {"nome": "Fernanda", "sexo": "F", "cabelo": "ruivo"},
    {"nome": "José", "sexo": "M", "cabelo": "careca"}
]


@app.route("/pessoa", methods=["POST"])
def cadastrar():
    pessoa = request.json
    pessoas.append(pessoa)
    return jsonify(pessoas)


if __name__ == "__main__":
    app.run(host="localhost", port=5002)
