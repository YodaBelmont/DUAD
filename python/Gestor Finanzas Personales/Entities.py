class Category():
    def __init__(self, category):
        self.category = category


class Transaction():
    def __init__(self, title, amount, transaction_type, category, date):
        self.title = title
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.date = date
