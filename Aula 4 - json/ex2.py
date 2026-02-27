import json

data = {
    "nome": "Maria",
    "idade": 20,
    "cidade": 'Minas Gerais'
}

with open('Exemplo2.json', 'w') as file:
    json.dump(data, file)
