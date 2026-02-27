# Exemplo 39

# Jogo de adivinhação
import random

numero_secreto = random.randint(1, 100)
tentativa = None

while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    if tentativa < numero_secreto:
        print("Muito baixo!")
    elif tentativa > numero_secreto:
        print("Muito alto!")

print("Parabéns! você adivinhou o número.")