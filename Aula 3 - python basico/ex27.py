# Exemplo 27

idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
historico_credito = input("Você tem um bom histórico de crédito? (sim/não): ").lower()

if idade >= 18 and renda_mensal >= 3000 and historico_credito == "sim":
    print("Você é elegível para o empréstimo.")
elif idade >= 18 and (renda_mensal >= 3000 or historico_credito == "sim"):
    print("Você pode ser elegível para um empréstimo com condições especiais.")
else:
    print("Você não é elegível para o empréstimo.")