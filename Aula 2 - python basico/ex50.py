# Exemplo 50

# construção da classe
class Pessoas:
    def __init__(self, nome, idade, UF):
        self.nome = nome
        self.idade = idade
        self.UF = UF

# Atributos
p1 = Pessoas("Gislene", 47, "Rio Grande do Sul")

# imprimindo
print(p1.nome)
print(p1.idade)
print(p1.UF)