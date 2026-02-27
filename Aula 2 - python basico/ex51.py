# Exemplo 51

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.ano} {self.marca} {self.modelo}"

# Criar uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
print(meu_carro.descricao())