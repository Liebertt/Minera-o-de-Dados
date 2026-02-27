import json

with open('Exemplo2c.json', 'r') as file:
    data = json.load(file)

nome = data['nome']
idade = data['idade']
profissao = data['profissao']

print(f'Nome: {nome}, Idade: {idade}, Profissão: {profissao}')

