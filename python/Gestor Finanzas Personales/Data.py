import csv
import os

def write_csv(headers, table_rows):
        try:
                with open("Transactions_data.csv", "w", encoding="utf-8") as file:
                        writer = csv.writer(file)
                        writer.writerow(headers)
                        writer.writerows(table_rows)
                return print("DATA SAVED SUCCESSFULLY")
        except Exception as error:
                print(f"ERROR {error}")



def import_csv():
        table_rows = []
        with open("Transactions_data.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                table_rows.append(reader)
        return table_rows 