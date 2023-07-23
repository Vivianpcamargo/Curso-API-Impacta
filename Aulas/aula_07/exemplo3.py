from flask import Flask

app = Flask(__name__)

casais_e_filhos = {
    "Camila,Paulo": ["Pedro", "Carlos", "Mariana"],
    "Laura,Joaquim": ["Sandra", "Daniela"],
    "Rafaela,Fernando": ["Larissa", "Marcos", "Vanessa", "Andressa"],
    "Maria,André": ["Juliano"],
    "Tatiana,Luís": ["Kelly", "Kelvin", "Karla"],
    "Beatriz,José": ["João", "Marcelo", "Guilherme"],
    "Tamara,Rodolfo": []
}


def filhos(mae, pai):
    casal = f"{mae},{pai}"
    if casal not in casais_e_filhos:
        return None
    filhos = casais_e_filhos[casal]
    if len(filhos) == 0:
        return "O casal não tem filhos."
    if len(filhos) == 1:
        return f"O casal tem 1 filho(a): {filhos[0]}."
    return f"O casal tem {len(filhos)} filhos(as): " \
        + f"{ ', '.join(filhos[:-1])} e {filhos[-1]}."


@app.route("/casal/<mae>/<pai>/filhos")
def encontrar_filhos(mae, pai):
    f = filhos(mae, pai)
    if f is None:
        return "Casal não encontrado."
    return f


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
