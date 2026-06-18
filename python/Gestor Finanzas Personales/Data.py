import csv


def write_csv(table_rows):
        try:
                with open("Transactions_data.csv", "w", encoding="utf-8", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(table_rows)
                return print("DATA SAVED SUCCESSFULLY")
        except Exception as error:
                print(f"ERROR {error}")


def import_csv():
        table_rows = []
        try:
                with open("Transactions_data.csv", "r", encoding="utf-8", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                                table_rows.append(row)
                        print("DATA SAVED SUCCESSFULLY")
                return table_rows
        except Exception as error:
                print(f"ERROR {error}")
