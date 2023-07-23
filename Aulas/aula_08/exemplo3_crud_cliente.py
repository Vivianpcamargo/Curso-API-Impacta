import requests


def entrada_dados():
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    cabelo = input("Digite a cor do cabelo: ")

    dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}

    return dados


def teste_post():
    dados = entrada_dados()
    x = requests.post("http://localhost:5002/pessoa", json=dados)
    if x.status_code != 200:
        print(f"[{x.status_code}] {x.text}")
    else:
        print(x.text)


def teste_put():
    id_pessoa = int(input('Digite o id da pessoa que deseja alterar: '))
    dados = entrada_dados()
    x = requests.put("http://localhost:5002/pessoa/" +
                     str(id_pessoa), json=dados)
    if x.status_code != 200:
        print(f"[{x.status_code}] {x.text}")
    else:
        print(x.text)


def teste_get_id():
    id_pessoa = int(input('Digite o id da pessoa que deseja buscar: '))
    x = requests.get("http://localhost:5002/pessoa/"+str(id_pessoa))
    if x.status_code != 200:
        print(f"[{x.status_code}] {x.text}")
    else:
        print(x.text)


def teste_delete():
    id_pessoa = int(input('Digite o id da pessoa que deseja excluir: '))
    x = requests.delete("http://localhost:5002/pessoa/"+str(id_pessoa))
    if x.status_code != 200:
        print(f"[{x.status_code}] {x.text}")
    else:
        print(x.text)


print('------------------------------------------\n')
print('Tentando a rota /pessoa com POST\n')
teste_post()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com POST novamente \n')
teste_post()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com PUT \n')
teste_put()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com GET e pessoa específica\n')
teste_get_id()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com DELETE\n')
teste_delete()
