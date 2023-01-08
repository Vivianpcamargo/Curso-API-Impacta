from flask import Flask, json        
app = Flask(__name__)         
from flask import jsonify
from flask import request


corredores = [{"nome": "Usain Bolt", "tempo": 9.63, "id": 14},
              {"nome": "Andreas Thorkildsen", "tempo": 12.5, "id": 35},
              {"nome": "Ryan Crouser", "tempo": 10.2, "id": 7},
              {"nome": "Sergey Litvinov", "tempo": 10.1, "id": 21}, ]

@app.route("/")                 #só que eu associei ela a uma URL
def hello():                    #função que retorna string
   return "Corredores"

#para ordenar os corredores por tempo
def tempo(dicionario_corredor):
    return dicionario_corredor['tempo']

@app.route("/corredores", methods=["GET"])
def lista_corredores():
    corredores.sort(key=tempo)
    return jsonify(corredores)

@app.route("/corredores", methods=["POST"])
def novo_corredor():
    dicionario = request.json
    corredores.append(dicionario)
    corredores.sort(key=tempo)
    return jsonify(corredores)


@app.route("/corredores/maior_tempo", methods=["GET"])
def consulta_por_tempo():
    corredores.sort(key=tempo)
    corredor = corredores[-1]
    return corredor

@app.route("/corredores/maior_tempo", methods=["DELETE"])
def remove_por_tempo():
    corredores.sort(key=tempo)
    corredor = corredores.pop()
    return {"removido": corredor}

#essas funções tem muito código em comum!
# você consegue melhorar isso??

@app.route("/corredores/<int:id_deletar>", methods=["DELETE"])
def remove_por_id(id_deletar):
    for corredor in corredores:
        if corredor['id'] == id_deletar:
            corredores.remove(corredor)
            return {"status": "ok"}
    return {"status": "nao encontrado"}, 404
    
@app.route("/corredores/<int:id_consulta>", methods=["GET"])
def exibe_por_id(id_consulta):
    for corredor in corredores:
        if corredor['id'] == id_consulta:
            return {"status": "ok", "corredor": corredor}
    return {"status": "nao encontrado"}, 404

@app.route("/corredores/<int:id_consulta>", methods=["PUT"])
def altera_por_id(id_consulta):
    dicionario = request.json
    for corredor in corredores:
        if corredor['id'] == id_consulta:
            if corredor['tempo'] < dicionario['tempo']:
                return {"status": "tempo de corrida superior ao record atual"}, 400
            corredor['tempo'] = dicionario['tempo']
            return {"status": "ok", "corredor": corredor}
    return {"status": "nao encontrado"}, 404

app.run()