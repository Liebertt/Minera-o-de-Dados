import json

def ler_arquivo_json(caminho):
    with open(caminho, 'r') as arquivo:
        return json.load(arquivo)

def escrever_arquivo_json(caminho, dados):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

caminho_arquivo = "Exemplo9.json"

dados = ler_arquivo_json(caminho_arquivo)

nome_para_atualizar = input("Digite o nome da pessoa que deseja atualizar: ")

for pessoa in dados['pessoas']:
    if pessoa['nome'].lower() == nome_para_atualizar.lower():
        nova_idade = int(input(f"Digite a nova idade para {pessoa['nome']} "))
        nova_cidade = input(f"Digite a nova cidade para {pessoa['nome']} ")
        pessoa['idade'] = nova_idade
        pessoa['cidade'] = nova_cidade
        break
else:
    print("Pessoa não encontrada.")

escrever_arquivo_json(caminho_arquivo, dados)

print("Dados atualizados com sucesso!")
