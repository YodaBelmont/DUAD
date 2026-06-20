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
    
    
    def to_row(self):
        return [self.title, 
                self.amount,
                self.transaction_type,
                self.category,
                self.date]


def get_income(table_rows, values):
    transaction = Transaction(values["title"], values["amount"], "income", values["category_list"], values["date"])
    table_rows.append(transaction.to_row())


def get_outcome(table_rows, values):
    transaction = Transaction(values["title"], values["amount"], "outcome", values["category_list"], values["date"])
    table_rows.append(transaction.to_row())


def get_category(category_list, title):
    category1 = Category(title) 
    category_list.append(category1.category)
