import requests

url = "https://api.openf1.org/v1/drivers"

resposta = requests.get(url)

print(resposta.status_code)

dados = resposta.json()

contador = 0

for piloto in dados:
    print(piloto["full_name"])

    contador += 1

    if contador == 10:
        break