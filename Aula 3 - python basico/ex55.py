# Exemplo 55

# Parte 1: Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

# Parte 2: Classe Inventario
class Inventario:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, producto):
        self.produtos.append(producto)

    def valor_total_inventario(self):
        return sum(produto.valor_total() for produto in self.produtos)

# Parte 3: Execução
# Criar instâncias das classes Produto e Inventario
produto1 = Produto("Laptop", 3000, 5)
produto2 = Produto("Mouse", 50, 20)
inventario = Inventario()

inventario.adicionar_produto(produto1)
inventario.adicionar_produto(produto2)

print(f"Valor total do inventário: R${inventario.valor_total_inventario():.2f}")