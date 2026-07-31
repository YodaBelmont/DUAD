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


    @property
    def category_names(self):
        return [category.category for category in self.categories]


    def check_data(self):
        if os.path.exists("Categories_list.csv"):

            rows = Data.import_category_list([])

            self.categories.clear()

            for row in rows:
                category = entity.Category(
                    row[0],
                    row[1]
                )

                self.categories.append(category)

            print("Category list updated")
            print(len(self.categories))

        if os.path.exists("Transactions_data.csv"):

                    rows = Data.import_csv([])
        
                    self.transactions.clear()
        
                    for row in rows:

                        selected_category = None

                        for category in self.categories:
                            if category.category == row[3]:
                                selected_category = category
                                break


                        transaction = entity.Transaction(
                            row[0],
                            row[1],
                            row[2],
                            selected_category,
                            row[4]
                        )
        
                        self.transactions.append(transaction)
        
                    print("Transactions updated")
    
    
    def save_data(self):
        Data.write_csv(self.table_rows)
        Data.write_category_list(self.categories)
    
    
    def create_transaction(self, transaction_type, values):
        transaction_category = None
        
        for category in self.categories:
            if category.category == values["category_list"]:
                transaction_category = category
                break

        transaction = entity.Transaction(values["title"], values["amount"], transaction_type, transaction_category, values["date"])
        self.transactions.append(transaction)
        Data.write_csv(self.table_rows)
    
    
    def has_categories(self):
        return bool(self.categories)
    
    
    def get_category(self,title, color):
        category1 = entity.Category(title, color)
        self.categories.append(category1)
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
        
        for transaction in self.transactions:
            if start_date <= transaction.date <= end_date:
                new_table.append(transaction)
        return new_table
    
    
    def color_rows(self, rows):
        row_colors = []
        for index, transactions in enumerate(rows):
            row_colors.append((index,"white",transactions.category.color))
        return row_colors
