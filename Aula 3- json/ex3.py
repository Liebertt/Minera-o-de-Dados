import json

with open('Exemplo2.json', 'r') as file:
    data = json.load(file)

data['idade'] = 56

with open('Exemplo2a.json', 'w') as file:
    json.dump(data, file)

