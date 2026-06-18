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


def get_transaction(entities_table, table_rows, values):
    transaction = Transaction(values["title"], values["amount"], values["types"], values["category_list"], values["date"])
    entities_table.append(transaction)
    table_rows.append(transaction.to_row())


def get_category(category_list, title):
    category1 = Category(title) 
    category_list.append(category1.category)
