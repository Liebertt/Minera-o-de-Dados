# Exemplo 54

class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

# Criar uma instância da classe Estudante
estudante = Estudante("Renata")
estudante.adicionar_nota(85)
estudante.adicionar_nota(90)
estudante.adicionar_nota(78)

print(f"Média de {estudante.nome}: {estudante.calcular_media():.2f}")