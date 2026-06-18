import FreeSimpleGUI as sg
import Entities as entity
import Data
def show_main_menu():
    headings = ["Title", "Amount", "Type", "Category" , "Date"]
    entities_table = []
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
        [sg.Button("REGISTER NEW TRANSACTION")],

        [sg.Text("IMPORT EXISTING FILES")],
        [sg.Button("Import", key="import")],


        [sg.Text("SAVE FILES")],
        [sg.Button("Save", key="save")]
        ]

    window = sg.Window("FINANCE MANAGEMENT", layout, size=(500,500))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "REGISTER NEW TRANSACTION":
            show_add_transaction_interface(entities_table,table_rows)
            window["table"].update(values=table_rows)

        if event == "save":
            Data.write_csv(table_rows)

        if event == "import":
            table_rows = Data.import_csv()
            window["table"].update(values=table_rows)

    window.close()


def show_create_category_interface():
    category_list = []
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
    return category_list



def show_add_transaction_interface(entities_table, table_rows):
    category_list = []
    layout = [
        [sg.Text("Transaction Type")],

        [sg.Combo(["Income" , "Outcome"], key="types", size=(10, 10), enable_events=True)],

        [sg.Text("Title")], [sg.Input(key="title")],
        [sg.Text("Amount")], [sg.Input(key="amount")],

        [sg.Text("Category")],
        [sg.Combo(category_list, key="category_list", size=(25, 25))],

        [sg.Button("Add category", key="Add")],

        [sg.CalendarButton("Select Date", target="date", format="%d/%m/%Y")],

        [sg.Input(key="date")],

        [sg.Button("Accept"), sg.Button("Cancel")],
    ]

    window = sg.Window("ADD TRANSACTION", layout, size=(500, 500))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        if event == "Add":
            category_list = show_create_category_interface()
            window["category_list"].update(values=category_list)

        if event == "Accept":
            if not values["title"] or not values["amount"] or not values["category_list"]:
                sg.popup("CANNOT LEAVE ANY BLANK SPACES")
            else:
                entity.get_transaction(entities_table, table_rows, values)
                sg.popup("Transaction Added")
                break
    window.close()
