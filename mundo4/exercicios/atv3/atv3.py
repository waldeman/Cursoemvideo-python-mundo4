class ContaBancaria:
    """
    Cria uma conta bancária que permite saques e depósitos"""

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"A conta {self.id} foi criada com sucesso, saldo atual de {self.saldo:,.2f}")

    def __str__(self):
        print("-"*30)
        print("\033[33mInformações da conta:\033[m".center(40))
        print("-"*30)
        return f"\033[34m-id = {self.id} \n-nome = {self.titular} \n-saldo = R${self.saldo:,.2f}\033[m"

    def depositar(self, valor):
        self.saldo += valor
        print(f"\033[32mDepósito de {valor:,.2f} autorizado na conta {self.id}\033[m]")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"\033[32mSaque de {valor:,.2f} autorizado na conta {self.id}\033[m")
        else:
            print(f"\033[31mSaque de {valor:,.2f} recusado na conta {self.id}: Saldo insuficiente\033[m")


conta1 = ContaBancaria(10001, "Waldeman", 1000)
conta1.sacar(5)
print(conta1)
