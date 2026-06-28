import csv


def write_csv(table_rows):
        try:
                with open("Transactions_data.csv", "w", encoding="utf-8", newline="") as file:
                        writer_rows = csv.writer(file)
                        writer_rows.writerows(table_rows)
        except Exception as error:
                print(f"ERROR {error}")


def import_csv():
        table_rows = []
        try:
                with open("Transactions_data", "r", encoding="utf-8", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                                table_rows.append(row)
        except Exception as error:
                print(f"ERROR {error}")


def write_category_list(category_list):
        try:
                with open("Categories_list.txt", "w", encoding="utf-8") as file:
                        for category in category_list:
                                file.write(category + "\n")
        except Exception as error:
                print(f"ERROR {error}")

def import_category_list():
        try:
                with open("Categories_list.txt", "r", encoding="utf-8") as file:
                        category_list = []
                        for line in file:
                                category_list.append(line.strip())
        except Exception as error:
                print(f"ERROR {error}")