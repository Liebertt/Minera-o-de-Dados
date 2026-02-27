# Exemplo 26

idade = int(input("Digite sua idade: "))
cidadania = input("Você é cidadão brasileiro? (sim/não): ").lower()

if idade >= 18 and cidadania == "sim":
    print("Você pode votar.")
elif idade < 18 and cidadania == "sim":
    print("Você ainda não pode votar.")
elif cidadania == "não":
    print("Apenas cidadãos brasileiros podem votar.")
else:
    print("Informações inválidas.")