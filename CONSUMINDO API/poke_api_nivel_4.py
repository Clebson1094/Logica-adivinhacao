import requests

url = "https://pokeapi.co/api/v2/pokemon/"
todos_os_nomes = []


while url:
    resposta = requests.get(url)
    dados = resposta.json()

    for pokemon in dados["results"]:
        todos_os_nomes.append(pokemon["name"])

    url = dados["next"]