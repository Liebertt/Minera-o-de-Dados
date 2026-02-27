# Exemplo 48

mensagem = "FATEC a melhor faculdade do Brasil"
vogais = "aeiouAEIOU"
contagem = 0
for letra in mensagem:
    if letra in vogais:
        contagem += 1
print("Número de vogais:", contagem)