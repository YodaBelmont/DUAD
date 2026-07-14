import csv


def write_csv(rows):
        if not rows:
                return print("THERE IS NO DATA TO SAVE")
        try:
                with open("Transactions_data.csv", "w", encoding="utf-8", newline="") as file:
                        writer_rows = csv.writer(file)
                        writer_rows.writerows(rows)
        except Exception as error:
                print(f"ERROR {error}")


def import_csv(rows):
        try:
                rows.clear()
                with open("Transactions_data.csv", "r", encoding="utf-8", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                                rows.append(row)
                        return rows
        except Exception as error:
                print(f"ERROR {error}")


def write_category_list(categories):
        if not categories:
                return print("THERE IS NO DATA TO SAVE")
        try:
                with open("Categories_list.txt", "w", encoding="utf-8") as file:
                        for category in categories:
                                file.write(category + "\n")
        except Exception as error:
                print(f"ERROR {error}")


def import_category_list(categories):
        try:
                categories.clear()
                with open("Categories_list.txt", "r", encoding="utf-8") as file:
                        for line in file:
                                categories.append(line.strip())
                        return categories
        except Exception as error:
                print(f"ERROR {error}")