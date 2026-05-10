class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_funds(self, amount):
        self.balance += amount
        print(f"Funds added: {amount}")

    def loan_funds(self, amount):
        if self.balance <= 0:
            raise Exception("THERE IS NO MONEY")
        self.balance -= amount
        print(f"Funds loaned: {amount}")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def loan_funds(self, amount):
        if (self.balance - amount) < self.min_balance:
            raise Exception("ACTION NOT ALLOwED")

        super().loan_funds(amount)


acc1 = BankAccount(1000)
acc2 = SavingsAccount(500, 1000)

acc1.add_funds(700)
acc2.loan_funds(400)

print(f"Normal acc balance: {acc1.balance}")
print(f"Savings acc balance: {acc2.balance}")
