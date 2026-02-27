import json

x = '{"nome": "Joao", "idade": 30, "cidade": "São Paulo"}'

y = json.loads(x)

print(y["nome"], y["idade"])
