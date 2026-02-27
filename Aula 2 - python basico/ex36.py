# Exemplo 36

string = "Faculdade de Tecnologia do Estado de São Paulo"
vogais = "aeiou"
i = 0
contagem = 0
while i < len(string):
    if string[i] in vogais:
        contagem += 1
    i += 1
print("Número de vogais: ", contagem)