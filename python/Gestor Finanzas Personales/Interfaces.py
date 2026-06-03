import FreeSimpleGUI as sg
import Entities as entity
def show_main_menu():
    headings = ["Title", "Amount", "Type", "Category" , "Date"]
    table_data = []
    layout = [
        [sg.Text("-" * 6), sg.Text("FINANCE SYSTEM MANAGEMENT"), sg.Text("-" * 6)],
        [sg.Table(
            values=table_data,
            headings=headings,
            auto_size_columns=False,
            num_rows=4,
            key="table",
            enable_events=True,
            justification="left",
            size=(100, 10))],
        [sg.Button("REGISTER NEW TRANSACTION")],
        ]

    window = sg.Window("FINANCE MANAGEMENT", layout, size=(500,500))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == "REGISTER NEW TRANSACTION":
            transaction = show_add_transaction_interface()
            table_data.append(transaction)
            table_rows = []
            
            for transaction in table_data:
                table_rows.append([transaction.title, transaction.amount, transaction.category])

            window["table"].update(values=table_rows)

    window.close()


def show_create_category_interface():
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
            category1 = entity.Category(values["title"])
            sg.popup("Category Added")
            window.close()
            break
    return category1


def get_table_data(window):
    table_data = []
    _ , values = window.read()
    
    for key, item in values.items():
        table_data.append([key,item])
    
    return table_data


def show_add_transaction_interface():
    category_list = []
    layout = [
        [sg.Text("Transaction Type")],
        
        [sg.Combo(["Income" , "Outcome"], key="types", size=(10, 10), enable_events=True)],
        
        [sg.Text("Title")], [sg.Input(key="title")],
        [sg.Text("Amount")], [sg.Input(key="amount")],
        
        [sg.Text("Category")],
        [sg.Combo(category_list, key="category_list", size=(25, 25))],
        
        [sg.Button("Add category", key="Add")],
        
        [sg.Checkbox("ENTER DATE MANUALLY", key="auto_date", enable_events=True)],
        
        [sg.Text("Date", key="date_text",visible=False)], [sg.Input(key="date",  visible=False)],
        
        
        
        [sg.Button("Accept"), sg.Button("Cancel")],
    ]
    
    window = sg.Window("ADD TRANSACTION", layout, size=(500, 500))
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        
        if event == "auto_date":
            boolean_value = values["auto_date"]
            
            window["date_text"].update(visible=boolean_value)
            window["date"].update(visible=boolean_value)
        
        
        if event == "Add":
            category = show_create_category_interface()
            category_list.append(category)
            titles = [category.category for category in category_list]
            window["category_list"].update(values=titles)
        
        
        if event == "Accept":
            if not values["title"] or not values["amount"] or not values["category_list"]:
                sg.popup("CANNOT LEAVE ANY BLANK SPACES")
            else:
                if values["types"] == "Income":
                    income = entity.Income(values["title"], values["amount"], values["types"])
                    sg.popup("Transaction Added")
                    window.close()
                    return income
                else:
                    outcome = entity.Outcome(values["title"], values["amount"], values["types"])
                    sg.popup("Transaction Added")
                    window.close()
                    return outcome



show_main_menu()