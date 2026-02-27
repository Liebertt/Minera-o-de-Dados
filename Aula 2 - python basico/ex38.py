# Exemplo 38

# verificando se número e primo!
num = 29
i = 2
is_prime = True
while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print(num, "é um número primo")
else:
    print(num, "não é um número primo")