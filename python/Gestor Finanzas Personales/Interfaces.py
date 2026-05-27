import FreeSimpleGUI as sg

def show_main_menu():
    headings = ["Type", "Amount", "Category" , "Date"]
    table_data = []
    layout = [
        [sg.Text("-" * 6), sg.Text("FINANCE SYSTEM MANAGEMENT"), sg.Text("-" * 6)],
        [sg.Table(
            values=table_data,
            headings=headings,
            auto_size_columns=True,
            num_rows=4,
            key="table",
            enable_events=True)],
        [sg.Button("REGISTER NEW TRANSACTION")],
        ]

    window = sg.Window("FINANCE MANAGEMENT", layout, size=(500,500))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == "REGISTER NEW TRANSACTION":
            show_add_transaction_interface()

    window.close()


def get_table_data(window):
    table_data = []
    _ , values = window.read()
    
    for key, item in values.items():
        table_data.append([key,item])
    
    return table_data


def show_add_transaction_interface():
    layout = [
        [sg.Text("Title")], [sg.Input(key="title")],
        [sg.Text("Amount")], [sg.Input(key="amount")],
        [sg.Text("Category")], [sg.Input(key="category")],
        
        [sg.Checkbox("USE TODAY¨S DATE", key="auto_date", enable_events=True)],
        
        [sg.Text("Date", key="date_text",visible=False)], [sg.Input(key="date",  visible=False)],
        
        [sg.Button("Accept")], [sg.Button("Cancel")]
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
        
        if event == "Accept":
            if not values["title"] or not values["amount"] or not values["category"]:
                sg.popup("CANNOT LEAVE ANY BLANK SPACES")
            else:
                data = []
                


show_main_menu()