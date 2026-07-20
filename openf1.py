import requests


def listar_pilotos():

    url = "https://api.openf1.org/v1/drivers"

    resposta = requests.get(url)
    
    
    return resposta.json()
    
import requests


def listar_corridas(ano):

    url = f"https://api.openf1.org/v1/meetings?year={ano}"


    resposta = requests.get(url)

    dados = resposta.json()
    
    #return resposta.json()

    corridas_tratadas = []

    for corrida in dados:

        corridas_tratadas.append(
            {"meeting_key": corrida["meeting_key"],
                               "circuit_key": corrida["circuit_key"],
                               "meeting_name": corrida["meeting_name"],
                               "meeting_official_name": corrida["meeting_official_name"],
                               "circuit_short_name": corrida["circuit_short_name"],
                               "country_name": corrida["country_name"],
                               "country_code": corrida["country_code"],
                               "is_cancelled": corrida["is_cancelled"],
                               "location": corrida["location"],
                               "date_start": corrida["date_start"],
                               "date_end": corrida["date_end"],
                               "year": corrida["year"]
            }
                               


                               
        )
    return corridas_tratadas