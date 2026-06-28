import FreeSimpleGUI as sg
import LogicManagement 
import Entities as entity
import Data
import os
def show_main_menu():
    manager = LogicManagement.Finance_Manager()
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

        manager.check_data(table_rows, window)

        if event == sg.WIN_CLOSED:
            manager.save_data(table_rows, category_list)
            break

        if event == "ADD OUTCOME":
            if not category_list:
                sg.popup("CANNOT ADD TRANSACTION\n NO CATEGORIES AVAILABLE")
                continue
            show_add_transaction_interface("OUTCOME", category_list, table_rows, window, values)

        if event == "ADD INCOME":
            if not category_list:
                sg.popup("CANNOT ADD TRANSACTION\n NO CATEGORIES AVAILABLE")
                continue
            show_add_transaction_interface("INCOME", category_list, table_rows, window, values)

        if event == "ADD CATEGORY":
            manager.show_category_interface(category_list)

    window.close()


def show_create_category_interface(category_list):
    manager = LogicManagement.Finance_Manager()
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
            manager.get_category(category_list, values["title"])
            sg.popup("Category Added")
            window.close()
            break



def show_add_transaction_interface(transaction_type, category_list, table_rows, window, values):
    manager = LogicManagement.Finance_Manager()
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

        manager.create_transaction(transaction_type, table_rows, category_list, window, values)

    window.close()
