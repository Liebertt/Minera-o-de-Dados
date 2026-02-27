# Exemplo 37

# Este código imprime os primeiros 10 números de Fibonacci
n = 10
a, b = 0, 1
i = 0
while i < n:
    print(a)
    a, b = b, a + b
    i += 1