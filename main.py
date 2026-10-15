from openf1 import listar_corridas

corridas = listar_corridas(2026)

#print(type(corridas))
#print(len(corridas))
#print(corridas[0])

for corrida in corridas:
    print(corrida["meeting_name"])

from openf1 import listar_sessoes

sessoes = listar_sessoes(1304)
for sessao in sessoes:
    print("Tipo de dado retornado:", type(sessoes))
print("Quantidade de sessões encontradas:", len(sessoes))

if len(sessoes) > 0:
    print("\nPrimeira sessão encontrada:")
    print(sessoes[0])