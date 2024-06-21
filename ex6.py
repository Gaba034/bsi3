class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def deposito(self, quantia):
        self.saldo += quantia
        return self.saldo

    def retirada(self, quantia):
        if quantia > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= quantia
        return self.saldo

class ContaPoupanca(ContaBancaria):
    taxa_juros = 0.03

class ContaCorrente(ContaBancaria):
    taxa_juros = 0.01

conta_poupanca = ContaPoupanca(1000)
conta_corrente = ContaCorrente(1000)

print(f"Saldo inicial : {conta_poupanca.saldo}")
print(f"Saldo + 500 na poupança: {conta_poupanca.deposito(500)}")
print(f"Saldo - 300 na poupança: {conta_poupanca.retirada(300)}")

print(f"Saldo inicial CC: {conta_corrente.saldo}")
print(f"Saldo CC + 200: {conta_corrente.deposito(200)}")
print(f"Saldo CC - 100: {conta_corrente.retirada(100)}")
