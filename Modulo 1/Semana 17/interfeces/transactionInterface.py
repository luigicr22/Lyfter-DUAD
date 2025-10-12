import FreeSimpleGUI as sg
from feature import features


def transaction_interface(account):
    
    list_category = features.list_categories(account)

    layout = [
        [sg.Text("Ingresar Transacción", font=("Calibri", 18))],
        [sg.Text("Fecha:"), sg.Input(key='input_date',size=10),sg.CalendarButton(key="date_button",button_text='Seleccionar Fecha',format="%Y-%m-%d")],
        [sg.Text("Detalle:"),sg.Input(key='input_details')],
        [sg.Text("Monto:"),sg.Input(key='input_amount')],
        [sg.Text("Categoria:"),sg.Combo(key = 'input_category', values = list_category)],
        [sg.Text("Tipo:"),sg.Combo(key = 'input_type', values = ['Ingreso','Gasto'])],
        [sg.Button('Aceptar'),sg.Button('Cancelar')],
        ]
    
    window = sg.Window('Ingresar Transacción', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        
        elif event == "Aceptar":
            try: 
                account = features.add_transaction(account, transaction_date=values['input_date'], details=values['input_details'], amount=values['input_amount'], category=values['input_category'],transaction_type=values['input_type']) 
                sg.popup ('Transacción agregada')
                break

            except Exception as e:
                sg.popup(e)
                continue
    
    window.close()
    return account