# dic = {
#     "musicas": [
#         {
#             "nome": "Hey Jude",
#             "banda": "Beatles",
#         },
#         {
#             "nome": "November Rain",
#             "banda": "Guns N' Roses",
#         },
#         {
#             "nome": "How Deep Is Your Love",
#             "banda": "Beatles",
#         },
#     ],
#     "filmes": {
#         "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira", "Magneto", "Ciclope", "Gambit"],
#         "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor", "Capitã Marvel", "Homem-Aranha"],
#         "Star Wars": ["Luke", "Leia", "C-3PO", "Darth Vader", "Obi-wan", "Yoda", "R2-D2", "Han Solo", "Chewbacca"],
#     }
# }


# def func1(a, b, c, d):
#     for x in a:
#         if x[b] == d:
#             return x[c]
#     return "nao sei"


engine = create_engine('sqlite:///imoveis.db')

class Imovel:
    def __init__(self, id, logradouro, numero, cep):
        # ...

def converte_dict_para_imovel(linha):
    d = dic (linha)
    return Imovel (**d)

def pesquisar (nome_rua):
    with engine.connect() as con:
        lista = [
            sql = ### lacuna1 ###
            rs = ### lacuna 2 ###
            ### lacuna 3 ###
                lista.append(converte_dict_para_imovel(linha))
            return lista
        ]