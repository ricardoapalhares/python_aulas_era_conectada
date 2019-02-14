import requests

data = {
    "nome": "Carlie",
    "idade": "2001-02-10 00:00:00",
    "telefone": "48-9997-6363",
    "profissao": "Terapeuta",
    "email": "carlie@gmail.com"
}

# recuperando o nome da api
response = requests.get('http://localhost:8000/pacientes/')
print(response.status_code, response.json()[0]['nome'])

# error 403
response_post = requests.post('http://localhost:8000/pacientes/', data=data, auth=('ricardo','0201'))
print(response_post.status_code)

# cadastrando um paciente (code=201)
response_post = requests.post('http://localhost:8000/pacientes/', data=data, auth=('ricardo','0202'))
print(response_post.status_code)
