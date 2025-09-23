import requests

# Faz uma requisição smples para um site
resposta = requests.get("https://api.github.com")
dados = resposta.json() #tenta converter JSON

print("Status", resposta.status_code)  #mostra o código da resposta
print(dados)
