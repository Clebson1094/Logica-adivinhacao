import requests

# Usuário que queremos buscar
usuario =  "OJailson17" # (Criador do Linux, só de exemplo)

# Fazendo a requisição na API do GitHub
url = f"https://api.github.com/users/{usuario}"
resposta = requests.get(url)

# Transforma em dicionário
dados = resposta.json()

# Exibe algumas informações
print("Nome", dados["name"])
print("Bio:", dados["bio"])
print("Número de repositórios públicos:", dados["public_repos"])
print("Número de seguidores", dados["followers"])
print("Localização", dados["location"])
print("Seguindo", dados["following"])