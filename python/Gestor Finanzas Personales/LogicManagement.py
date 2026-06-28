import Data
import Interfaces as interface
import FreeSimpleGUI as sg
import Entities as entity
import os



class Finance_Manager():
    def __init__(self):
        pass
    
    
    def check_data(self, table_rows ,window):
        if os.path.exists("Transactions_data.csv") and os.path.exists("Categories_list.csv"):
            Data.import_category_list()
            Data.import_csv()
            window["table"].update(values=table_rows)
            return print("IMPORT SUCCESS")
        return print("NO DATA TO IMPORT")
    
    
    def save_data(self, table_rows, category_list):
        Data.write_csv(table_rows)
        Data.write_category_list(category_list)
    
    
    def create_transaction(self, category_list, table_rows, window, transaction_type):
        while True:
            if not category_list:
                sg.popup("CANNOT ADD TRANSACTION\n NO CATEGORIES AVAILABLE")
                break
            if transaction_type == "INCOME":
                interface.show_add_transaction_interface(transaction_type, table_rows, category_list)
                window["table"].update(values=table_rows)
                Data.write_csv(table_rows)
                break
            interface.show_add_transaction_interface(transaction_type, table_rows, category_list)
            window["table"].update(values=table_rows)
            Data.write_csv(table_rows)
            break
    
    
    def show_category_interface(self, category_list):
        interface.show_create_category_interface(category_list)
        Data.write_category_list(category_list)
        print(category_list)
    
    
    def get_category(self, category_list, title):
        entity.get_category(category_list, title)
    
    
    def add_income(self, table_rows, values):
        entity.get_income(table_rows, values)
    
    
    def add_outcome(self, table_rows, values):
        entity.get_outcome(table_rows, values)
    
    