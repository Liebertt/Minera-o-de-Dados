# Exemplo 57

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

resultado = par_ou_impar(7)
print(f"O número é: {resultado}")
