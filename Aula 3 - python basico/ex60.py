# Exemplo 60

# frase ou palavra que se pode ler,
# da esquerda para a direita ou vice-versa

def palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

resultado = palindromo("Apos a sopa")
print(f"É palavra ou frase é palíndromo? {resultado}")