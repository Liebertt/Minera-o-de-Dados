import json
import os



def ler_arquivo_json(caminho):
    with open(caminho, 'r') as arquivo:
        return json.load(arquivo)

def escrever_arquivo_json(caminho, dados):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

caminho_arquivo = 'Exemplo9.json'

dados = ler_arquivo_json(caminho_arquivo)

novo_nome = input("Digite o nome: ")
nova_idade = int(input("Digite a idade: "))
nova_cidade = input("Digite a cidade: ")

nova_pessoa = {
    "nome": novo_nome,
    "idade": nova_idade,
    "cidade": nova_cidade
}
dados['pessoas'].append(nova_pessoa)

escrever_arquivo_json(caminho_arquivo, dados)

print("Dados atualizados com sucesso!")



