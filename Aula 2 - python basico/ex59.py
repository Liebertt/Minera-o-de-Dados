# Exemplo 59

def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = [10, 20, 30, 40, 50]
resultado = maior_numero(numeros)
print(f"O maior número é: {resultado}")