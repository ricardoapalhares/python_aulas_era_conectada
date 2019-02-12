import requests
from decimal import Decimal

response = requests.get('https://brasil.io/api/dataset/eleicoes-brasil/bens_candidatos/data')
results = response.json()['results']
proximo = response.json()['next']

print(response.status_code)

soma = 0
for element in results:
    soma += Decimal(element['valor_bem'])
    
    
media = round(soma/len(results),2)


print("O valor total dos bens: " + str(soma))
print("Média dos bens: " + str(media))

print(response.json()['next'])
