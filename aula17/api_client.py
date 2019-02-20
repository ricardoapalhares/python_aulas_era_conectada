import requests

data = {
    "nome": "Fabio Cartela",
    "idade": "1971-01-16 00:00:00",
    "telefone": "47-9877-2222",
    "profissao": "Chefão",
    "email": "Fabio@gmail.com"
}

# paciente = {
#     "nome": "Carlos Marin",
#     "idade": "1971-01-16 00:00:00",
#     "telefone": "47-9877-2222",
#     "profissao": "Chefão",
#     "email": "carlos@gmail.com"
# }

# paciente2 = {
#     "nome": "Clarice Maria",
#     "idade": "1966-01-16 00:00:00",
#     "telefone": "47-9877-2222",
#     "profissao": "Chefão",
#     "email": "clarice@gmail.com"
# }

# pacientes_list = {'pacientes': [paciente]}
# pacientes_list['pacientes'].append(paciente2);

# recuperando o nome da api
#response = requests.get('http://localhost:8000/pacientes/')
#print(response.status_code, response.json()[0]['nome'])

# error 403
#response_post = requests.post('http://localhost:8000/pacientes/', data=data, auth=('ricardo','0201'))
#print(response_post.status_code)

# cadastrando um paciente (code=201)
#response_post = requests.post('http://localhost:8000/pacientes/', data=data, auth=('ricardo','0202'))
#print(response_post.status_code)

url_pacientes = 'http://localhost:8000/pacientes/'
# url_pacientes = 'http://192.168.0.36:8000/pacientes/'

for n in range(400): 
    # response_post = requests.post(url_pacientes, data=data, auth=('mario','96384270mario'))
    response_post = requests.post(url_pacientes, data=data, auth=('ricardo','0202'))
    print(response_post.status_code)




