from datetime import datetime

class Category():
    def __init__(self, category):
        self.category = category
    
    
    def get_category(self):
        return self.category


class Transaction():
    def __init__(self, title, amount, transaction_type, category, date):
        self.title = title
        self.amount = float(amount)
        self.transaction_type = transaction_type
        self.category = category
        self.date = datetime.strptime(date, "%d/%m/%Y").date()
    
    
    def to_row(self):
        return [self.title, 
                self.amount,
                self.transaction_type,
                self.category,
                self.date.strftime("%d/%m/%Y")]


