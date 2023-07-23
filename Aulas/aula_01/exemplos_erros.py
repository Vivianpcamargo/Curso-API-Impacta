dic = {
    "alimentos": {
        "pizzas": [
            "margueritta",
            "mussarella",
            "frango com catupiry",
            "portuguesa",
        ],
        "bolos": (
            "floresta negra",
            "red velvet",
            "de laranja",
            "da vó",
        ),
        "calorias": {
            "leite": 129,
            "fatia pizza": 320,
            "agua": 0,
            "maça": 95,
        }
    },
    "linguagens": [
        {
            "nome": "javascript",
            "criacao": 1996,
            "paradigma": [
                "eventos",
                "funcional",
            ]
        },
        {
            "nome": "python",
            "criacao": 1991,
            "paradigma": [
                "orientada a objetos",
                "estruturada",
            ]
        },
        {
            "nome": "haskell",
            "criacao": 1990,
            "paradigma": [
                "funcional",
            ]
        }
    ]
}

# Só se aprende fazendo. PAUSE O VIDEO E TENTE RESPONDER!
# Se possível, FAÇA JUNTO NO SEU COMPUTADOR

# 1. quantas chaves tem o dicionario dic?
# Resposta: 2
print("r1", len((dic)))

# 2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
# Resposta: lista
print("r2", type((dic['linguagens'])))

# 3. como eu faço para mostrar todos os bolos?
# Resposta: print("r3", dic['alimentos']['bolos'])
print("r3", dic['alimentos']['bolos'])

# 4. qual é o tipo da lista de todos os bolos?
# Resposta: tupla
print("r4", type((dic['alimentos']['bolos'])))

# 5. o que o seguinte acesso imprime? Se ele dá erro, qual é o erro? Se dá erro, como corrigir?
# # print("r5", dic['linguagens']['javascript']['criacao'])
# Resposta: dá erro, e o correto seria print("r5", dic['linguagens'][0]['criacao'])

# 6. o que o seguinte acesso imprime? Se ele dá erro, qual é o erro? Se dá erro, como corrigir?
print("r6", dic['linguagens'][2] == "haskell")
# Resposta: não dá erro, mas para a validação dar true o correto seria print("r6", dic['linguagens'][2]['nome'] == "haskell")

# 7. o que o seguinte acesso imprime? Se ele dá erro, qual é o erro? Se dá erro, como corrigir?
print("r7", dic['alimentos']["pizzas"][2] == "mussarella")
# Resposta: não dá erro, mas para a validação dar true o correto seria print("r7", dic['alimentos']["pizzas"][1] == "mussarella")

# 8. o que o seguinte acesso imprime? Se ele dá erro, qual é o erro? Se dá erro, como corrigir?
print("r8", 1996 in dic['linguagens'][0])
# Resposta: a validação dá false, pois o in verifica se tem 1996 nas chaves não nos valores

# 9. o que o seguinte acesso imprime? Se ele dá erro, qual é o erro? Se dá erro, como corrigir?
print("r9", "criacao" in dic['linguagens'][0])
# Resposta: a validação dá true

# 9. o que o seguinte acesso imprime? Se ele dá erro, qual é o erro? Se dá erro, como corrigir?
# # print("r9v2", "pudim" in dic['sobremesas']["doces"])
# Resposta: a validação dá erro, pois o chave 'sobremesas' não existe

# 10. escreva uma função "mais velha" que recebe um dicionário como dic e retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista
# Resposta:


def mais_velha(dic):
    lista_linguagens = dic['linguagens']
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        if linguagem["criacao"] < ling_velha['criacao']:
            ling_velha = linguagem
    return ling_velha


print("r10", mais_velha(dic))

# 11. escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação
# Resposta:


def lista_paradigmas(dic):
    lista_linguagens = dic['linguagens']
    paradigmas = []
    for linguagem in lista_linguagens:
        paradigmas_da_linguagem = linguagem['paradigma']
        for p in paradigmas_da_linguagem:
            if p not in paradigmas:
                paradigmas.append(p)
    return paradigmas


print("r11", lista_paradigmas(dic))
