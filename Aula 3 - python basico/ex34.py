# Exemplo 34

# Solicita ao usuário um número
numero = int(input("Digite um número maior que 10: "))

# Decrementa o número até 0
while numero >= 0:
    print(f"Número: {numero}")
    numero -= 1  # Decrementa o número em 1 a cada iteração

print("Decremento encerrado.")