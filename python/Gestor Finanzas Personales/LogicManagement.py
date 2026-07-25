from datetime import datetime
import Data
import Entities as entity
import os



class Finance_Manager():
    def __init__(self):
        self.categories = []
        self.transactions = []
    
    
    @property
    def table_rows(self):
        return [transaction.to_row() for transaction in self.transactions]
    
    
    def check_data(self):
        if os.path.exists("Transactions_data.csv"):

            rows = Data.import_csv([])

            self.transactions.clear()

            for row in rows:
                transaction = entity.Transaction(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )

                self.transactions.append(transaction)

            print("Transactions updated")

        if os.path.exists("Categories_list.txt"):
            self.categories = Data.import_category_list(self.categories)
            print("Category list updated")
    
    
    def save_data(self):
        Data.write_csv(self.table_rows)
        Data.write_category_list(self.categories)
    
    
    def create_transaction(self, transaction_type, values):
        transaction = entity.Transaction(values["title"], values["amount"], transaction_type, values["category_list"], values["date"])
        self.transactions.append(transaction)
        Data.write_csv(self.table_rows)
    
    
    def has_categories(self):
        return bool(self.categories)
    
    
    def get_category(self,title, color):
        category1 = entity.Category(title)
        dict1 = {"CATEGORY": category1,
                "COLOR":color}
        self.categories.append(category1.get_category())
        Data.write_category_list(self.categories)
    
    
    def to_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    
    def check_values(self, values):
        required = ("title", "amount", "category_list", "date")
        return all(values[key] for key in required)
    
    
    def validate_date(self, date_str):
        try:
            entered_date = datetime.strptime(date_str, "%d/%m/%Y").date()
            today = datetime.today().date()

            if entered_date > today:
                return False
            return True

        except ValueError:
            return False
    
    
    def filter_table(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
        
        new_table = []
        
        for transaction in self.table_rows:
            if start_date <= transaction.date <= end_date:
                new_table.append(transaction)
        return new_table
