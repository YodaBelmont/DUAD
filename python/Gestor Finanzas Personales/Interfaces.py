import FreeSimpleGUI as sg
import LogicManagement 
import Data

manager = LogicManagement.Finance_Manager()


def show_main_menu():
    manager.check_data()
    layout = [
        [sg.Text("-" * 6), sg.Text("FINANCE MANAGEMENT SYSTEM"), sg.Text("-" * 6)],
        [sg.Table(
            values=manager.table_rows,
            headings=["Title", "Amount", "Type", "Category" , "Date"],
            auto_size_columns=False,
            num_rows=4,
            key="table",
            row_colors=manager.color_rows(manager.transactions),
            enable_events=True,
            justification="left",
            size=(100, 10))],
        [sg.Button("ADD CATEGORY")],

        [sg.Button("ADD INCOME")],

        [sg.Button("ADD OUTCOME")],

        [sg.Text("FILTER FROM: "), sg.Input(key="start_date", size=(10,1)), sg.CalendarButton("Select Date", target="start_date", format="%d/%m/%Y")],


        [sg.Text("TO: "), sg.Input(key="end_date", size=(10,1)), sg.CalendarButton("Select Date", target="end_date", format="%d/%m/%Y")],
        [sg.Button("FILTER")], [sg.Button("RESET FILTER"), sg.Button("GENERATE REPORT")]
        
        ]

    main_window = sg.Window("FINANCE MANAGEMENT", layout, size=(700,700))
    while True:
        event, values = main_window.read()

        if event == sg.WIN_CLOSED:
            manager.save_data()
            break

        if event == "ADD OUTCOME":
            if manager.has_categories():
                show_add_transaction_interface("OUTCOME", main_window)
            else:
                sg.popup("NO CATEGORIES AVAILABLE")

        if event == "ADD INCOME":
            if manager.has_categories():
                show_add_transaction_interface("INCOME", main_window)
            else:
                sg.popup("NO CATEGORIES AVAILABLE")

        if event == "ADD CATEGORY":
            show_create_category_interface()
        
        if event == "FILTER":
            if not manager.validate_date(values["start_date"]) or not manager.validate_date(values["end_date"]):
                sg.popup("ENTER A VALID DATE")
                continue
            filtered = manager.filter_table(values["start_date"], values["end_date"])
            main_window["table"].update(values=[transaction.to_row() for transaction in filtered], row_colors=manager.color_rows(filtered))
        
        if event == "RESET FILTER":
            main_window["table"].update(values= manager.table_rows, row_colors=manager.color_rows(manager.transactions))
        
        if event == "GENERATE REPORT":
            Data.generate_report(manager.table_rows, manager.transactions)

    main_window.close()


def show_create_category_interface():
    layout = [
        [sg.Text("Title")], [sg.Input(key="title")],
        [sg.ColorChooserButton("Color: ",target="color"), sg.Input(key="color", size=(10,1))],
        [sg.Button("Add")],
    ]

    window = sg.Window("ADD CATEGORY", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Add":
            manager.get_category(values["title"], values["color"])
            sg.popup("Category Added")
            window.close()
            break


def show_add_transaction_interface(transaction_type, main_window):
    layout = [

        [sg.Text("Title")], [sg.Input(key="title")],
        [sg.Text("Amount")], [sg.Input(key="amount")],

        [sg.Text("Category")],
        [sg.Combo(manager.category_names, key="category_list", size=(25, 25))],

        [sg.CalendarButton("Select Date", target="date", format="%d/%m/%Y")],

        [sg.Input(key="date")],

        [sg.Button("Accept"), sg.Button("Cancel")],
    ]

    transactions_window = sg.Window("ADD TRANSACTION", layout, size=(500, 500))
    while True:
        event, values = transactions_window.read()

        transactions_window["category_list"].update(values= manager.category_names)

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        if event == "Accept":
            if not manager.check_values(values):
                sg.popup("CANNOT LEAVE ANY BLANK SPACES")
                continue
            if not manager.to_float(values["amount"]):
                sg.popup("AMOUNT MUST BE A NUMBER")
                continue
            if not manager.validate_date(values["date"]):
                sg.popup("ENTER A VALID DATE")
                continue
            manager.create_transaction(transaction_type, values)
            main_window["table"].update(values=manager.table_rows, row_colors=manager.color_rows(manager.transactions))
            break

    transactions_window.close()
