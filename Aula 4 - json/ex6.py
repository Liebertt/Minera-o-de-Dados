import json
import os

ARQUIVO = "Exemplo6.json"

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'w', encoding="utf-8") as f:
        json.dump([], f, indent=2, ensure_ascii=False)

with open(ARQUIVO, "r", encoding='utf-8') as f:
    data = json. load(f)

if isinstance(data, dict):
    data = [data]

data = [item for item in data if item.get("nome") !="Pedro"]

with open(ARQUIVO, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('Registro excluido com sucesso!')
