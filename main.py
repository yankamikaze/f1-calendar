from openf1 import listar_corridas, listar_sessoes

# 1. Teste de Corridas da Temporada
corridas = listar_corridas(2026)

#print(type(corridas))
#print(len(corridas))
#print(corridas[0])

# Imprime o nome de cada evento/corrida
for corrida in corridas:
    print(corrida["meeting_name"])

# 2. Teste de Sessões de um Evento (ex: Pré-Temporada - meeting_key 1304)
sessoes = listar_sessoes(1304)
for sessao in sessoes:
    print("Tipo de dado retornado:", type(sessoes))
print("Quantidade de sessões encontradas:", len(sessoes))

if len(sessoes) > 0:
    print("\nPrimeira sessão encontrada:")
    print(sessoes[0])