import requests
import poke_api_nivel_4

tipos = []
pokemons = poke_api_nivel_4

for i in range(0, 1302):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemons.todos_os_nomes[i]}"
    resposta = requests.get(url)
    dados = resposta.json()
    i = i + 1
    for tipo in dados["types"]:
        if tipo["type"]["name"] not in tipos:
            tipos.append(tipo["type"]["name"])

print(tipos)