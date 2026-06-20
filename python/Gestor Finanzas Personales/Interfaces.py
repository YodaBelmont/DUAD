import FreeSimpleGUI as sg
import Entities as entity
import Data
import os
def show_main_menu():
    changes_made = False
    category_list = []
    headings = ["Title", "Amount", "Type", "Category" , "Date"]
    table_rows = []
    layout = [
        [sg.Text("-" * 6), sg.Text("FINANCE SYSTEM MANAGEMENT"), sg.Text("-" * 6)],
        [sg.Table(
            values=table_rows,
            headings=headings,
            auto_size_columns=False,
            num_rows=4,
            key="table",
            enable_events=True,
            justification="left",
            size=(100, 10))],
        [sg.Button("ADD CATEGORY")],

        [sg.Button("ADD INCOME")],

        [sg.Button("ADD OUTCOME")],

        ]

    window = sg.Window("FINANCE MANAGEMENT", layout, size=(500,500))

    while True:
        event, values = window.read()

        if os.path.exists("Transactions_data.csv") and os.path.exists("Categories_list.csv"):
            Data.import_category_list()
            Data.import_csv()
            window["table"].update(values=table_rows)

        if event == sg.WIN_CLOSED:
            Data.write_csv(table_rows)
            Data.write_category_list(category_list)
            break

        if event == "ADD OUTCOME":
            if not category_list:
                sg.popup("CANNOT ADD TRANSACTION\n NO CATEGORIES AVAILABLE")
                continue
            show_add_transaction_interface("OUTCOME", table_rows, category_list)
            window["table"].update(values=table_rows)
            Data.write_csv(table_rows)

        if event == "ADD INCOME":
            if not category_list:
                sg.popup("CANNOT ADD TRANSACTION\n NO CATEGORIES AVAILABLE")
                continue
            show_add_transaction_interface("INCOME", table_rows, category_list)
            window["table"].update(values=table_rows)
            Data.write_csv(table_rows)

        if event == "ADD CATEGORY":
            show_create_category_interface(category_list)
            Data.write_category_list(category_list)
            print(category_list)

        # if event == "save":
        #     Data.write_csv(table_rows)

        # if event == "import":
        #     table_rows = Data.import_csv("Transactions_data.csv")
        #     window["table"].update(values=table_rows)
        #     category_list = Data.import_csv("Categories_list.csv")

    window.close()


def show_create_category_interface(category_list):
    layout = [
        [sg.Text("Title")], [sg.Input(key="title")],

        [sg.Button("Add")],
    ]

    window = sg.Window("ADD CATEGORY", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Add":
            entity.get_category(category_list, values["title"])
            sg.popup("Category Added")
            window.close()
            break



def show_add_transaction_interface(transaction_type, table_rows, category_list):
    layout = [

        [sg.Text("Title")], [sg.Input(key="title")],
        [sg.Text("Amount")], [sg.Input(key="amount")],

        [sg.Text("Category")],
        [sg.Combo(category_list, key="category_list", size=(25, 25))],

        [sg.CalendarButton("Select Date", target="date", format="%d/%m/%Y")],

        [sg.Input(key="date")],

        [sg.Button("Accept"), sg.Button("Cancel")],
    ]

    window = sg.Window("ADD TRANSACTION", layout, size=(500, 500))

    while True:
        event, values = window.read()

        window["category_list"].update(values= category_list)

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        if event == "Accept":
            if not values["title"] or not values["amount"]:
                sg.popup("CANNOT LEAVE ANY BLANK SPACES")
                continue
            elif transaction_type == "INCOME":
                entity.get_income(table_rows, values)
                sg.popup("Transaction Added")
                break
            elif transaction_type == "OUTCOME":
                entity.get_outcome(table_rows, values)
                sg.popup("Transaction Added")
                break
    window.close()
