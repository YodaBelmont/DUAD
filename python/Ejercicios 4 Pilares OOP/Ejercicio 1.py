class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_funds(self, amount):
        self.balance += amount

    def loan_funds(self, amount):
        if self.balance <= 0:
            raise Exception("THERE IS NO MONEY")
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance

    def loan_funds(self, amount):
        if (self.balance - amount) < self.min_balance:
            print("ACTION NOT ALLOwED")
            return

        self.min_balance -= amount
        print(f"FUNDS LEFT: {self.min_balance}")
