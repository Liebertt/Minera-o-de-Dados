import json

def ler_arquivo_json(caminho):
    with open(caminho, 'r') as arquivo:
        return json.load(arquivo)

def escrever_arquivo_json(caminho, dados):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

caminho_arquivo = 'Exemplo9.json'

dados = ler_arquivo_json(caminho_arquivo)

nome_para_excluir = input("Digite o nome da pessoa que deseja excluir? ")

for pessoa in dados['pessoas']:
    if pessoa['nome'].lower() == nome_para_excluir.lower():
        dados['pessoas'].remove(pessoa)
        break
else:
    print("Pessoas não encontrada")

escrever_arquivo_json(caminho_arquivo, dados)

print("Dados atualizados com sucesso!")

