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
                with open("Categories_list.csv", "w", encoding="utf-8", newline="") as file:
                        writer = csv.writer(file)
                        for category in categories:
                                writer.writerow([category.category, category.color])
        except Exception as error:
                print(f"ERROR {error}")


def import_category_list(rows):
        try:
                rows.clear()
                with open("Categories_list.csv", "r", encoding="utf-8", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                                rows.append(row)
                        return rows
        except Exception as error:
                print(f"ERROR {error}")


def generate_report(rows, transactions):
        if not rows:
                return print("NO INFO")
        try:
                total_income = 0
                total_outcome = 0
                for transaction in transactions:
                        if transaction.transaction_type == "INCOME":
                                total_income += transaction.amount
                                continue
                        total_outcome += transaction.amount
                        
                with open("Report.csv", "w" , encoding="utf-8", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(("Title", "Amount", "Type", "Category" , "Date"))
                        writer.writerows(rows)
                        
                        writer.writerow(["\nTRANSACTIONS"])
                        writer.writerow([f"TOTAL INCOME: {total_income}"])
                        writer.writerow([f"TOTAL OUTCOME: {total_outcome}"])
                        writer.writerow([f"OVERALL TOTAL: {total_income+total_outcome}"])
        except Exception as error:
                print(error)