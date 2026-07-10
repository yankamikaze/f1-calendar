#import requests


#def listar_pilotos():

    #url = "https://api.openf1.org/v1/drivers"

    #resposta = requests.get(url)
    
    
    #return resposta.json()
    
import requests


def listar_corridas(ano):

    url = f"https://api.openf1.org/v1/meetings?year={ano}"


    resposta = requests.get(url)

    
    return resposta.json()
    