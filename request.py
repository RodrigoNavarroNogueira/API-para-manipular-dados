import requests

def get_total_de_vendas():
    link = 'http://127.0.0.1:5000/pegarvendas'

    requisicao = requests.get(link)

    print(requisicao)
    print(requisicao.json())

    resposta = requisicao.json()

    print(resposta['total de vendas'])


# get_total_de_vendas()


def get_total_tv():
    link = 'http://127.0.0.1:5000/pegarvendasum'

    requisicao = requests.get(link)

    print(requisicao)
    print(requisicao.json())

    resposta = requisicao.json()

    print(resposta['total de vendas da tv'])


get_total_tv()
