import requests
import poke_api_nivel_4
import colorama

colorama.init(autoreset=True)

while True:
    nome = str(input("Digite o nome do pokemon: ")).lower()
    if nome not in [n.lower() for n in poke_api_nivel_4.todos_os_nomes]:
        print("Nome não encontrado na lista de pokemon, tente novamente")
        continue
    break
    
url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

resposta = requests.get(url)

dados = resposta.json()
contagem_abilidades = len(dados["abilities"])

altura_em_metros = dados["height"] / 10
peso_em_kg = dados["weight"] / 10

print("Nome", dados["name"].title())
print("Altura", altura_em_metros, "m")
print("Peso", peso_em_kg, "kg")
print("Quantidade de Habilidades", contagem_abilidades)
'''print("Tipagem", dados["types"])
print("Habilidades", dados["abilities"])'''

for habilidade in dados["abilities"]:
    print("Habilidade", habilidade["ability"]["name"])

for tipo in dados["types"]:
    print("Tipagem", tipo["type"]["name"])
