import json

with open('Exemplo8.json', 'r') as arquivo:
    dados = json.load(arquivo)

indice = 0

while indice < len(dados['pessoas']):
    pessoas = dados['pessoas'][indice]
    print(f"Nome: {pessoas['nome']}")
    print(f"Idade: {pessoas['idade']}")
    print(f"Cidade: {pessoas['cidade']}")
    print("-" * 20)
    indice += 1