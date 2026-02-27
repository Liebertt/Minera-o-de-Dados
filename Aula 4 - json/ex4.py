import json

with open("Exemplo2.json", 'r') as file:
    data = json.load(file)

data['profissao'] = 'Engenheira'

with open('Exemplo2b.json', 'w') as file:
    json.dump(data, file)



