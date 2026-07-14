import Data
import Entities as entity
import os



class Finance_Manager():
    def __init__(self):
        self.categories = []
        self.table_rows = []
    
    
    def check_data(self):
        if os.path.exists("Transactions_data.csv"):
            self.table_rows = Data.import_csv(self.table_rows)
            print("Table rows updated")
        if os.path.exists("Categories_list.txt"):
            self.categories = Data.import_category_list(self.categories)
            print("Category list updated")
        else:
            return print("NO DATA")
    
    
    def save_data(self):
        Data.write_csv(self.table_rows)
        Data.write_category_list(self.categories)
    
    
    def create_transaction(self, transaction_type, values):
        transaction = entity.Transaction(values["title"], values["amount"], transaction_type, values["category_list"], values["date"])
        self.table_rows.append(transaction.to_row())
        Data.write_csv(self.table_rows)
    
    
    def has_categories(self):
        return bool(self.categories)
    
    
    def get_category(self,title):
        category1 = entity.Category(title)
        self.categories.append(category1.category)
        Data.write_category_list(self.categories)
