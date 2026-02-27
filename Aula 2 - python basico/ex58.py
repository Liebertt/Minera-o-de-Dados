# Exemplo 58

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(f"O fatorial é: {resultado}")