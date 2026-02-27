# Exemplo 52

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, quantia):
        self.saldo += quantia

    def sacar(self, quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        return f"Saldo da conta {self.titular}: R${self.saldo}"

# Criar uma instância da classe ContaBancaria
conta = ContaBancaria("Maria", 1000)
conta.depositar(500)
conta.sacar(200)
print(conta.mostrar_saldo())