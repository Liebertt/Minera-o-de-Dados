# Exemplo 35

# M.D.C. do números abaixo:
a = 48
b = 18
while b != 0:
    a, b = b, a % b
print("O maior divisor comum é: ", a)