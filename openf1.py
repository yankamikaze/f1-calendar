import requests

#TRAZ OS PILOTOS DA API OPENF1 - INICIO

def listar_pilotos():

    url = "https://api.openf1.org/v1/drivers"

    resposta = requests.get(url)
    resposta.raise_for_status()
    
    return resposta.json()
    
#TRAZ OS PILOTOS DA API OPENF1 - FIM

#TRAZ A LISTA DE CORRIDAS DA API OPENF1 - INICIO

def listar_corridas(ano):

    url = f"https://api.openf1.org/v1/meetings?year={ano}"


    resposta = requests.get(url)
    resposta.raise_for_status()
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


#TRAZ A LISTA DE CORRIDAS DA API OPENF1 - FIM



#TRAZ A LISTA DE SESSOES DE UM EVENTO DA API OPENF1 - INICIO

def listar_sessoes(meeting_key):

        url = f"https://api.openf1.org/v1/sessions?meeting_key={meeting_key}"

        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()


        sessoes_tratadas = []

        for sessao in dados:

            sessoes_tratadas.append(
                {"session_key": sessao["session_key"],
                 "meeting_key": sessao["meeting_key"],
                 "session_name": sessao["session_name"],
                 "session_type": sessao["session_type"],
                 "date_start": sessao["date_start"],
                 "date_end": sessao["date_end"],
                 "is_cancelled": sessao["is_cancelled"],
                 "location": sessao["location"],
                 "country_name": sessao["country_name"],
                 "country_code": sessao["country_code"],
                 "year": sessao["year"],
                 "gmt_offset": sessao["gmt_offset"]
                 }
            )
        return sessoes_tratadas

#TRAZ A LISTA DE SESSOES DE UM EVENTO DA API OPENF1 - FIM