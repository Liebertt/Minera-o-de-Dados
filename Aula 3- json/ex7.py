import json

def validar_json(json_data):
    try:
        json.loads(json_data)
        return True
    except ValueError as e:
        return False

with open('Exemplo6.json', 'r') as file:
    data = file.read()

if validar_json(data):
    print('O arquivo JSON é válido!')
else:
    print('O arquivo json é inválido')

