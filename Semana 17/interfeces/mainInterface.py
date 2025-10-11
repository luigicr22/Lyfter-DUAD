import FreeSimpleGUI as sg
from feature import features
from feature import persistence
from interfeces.categoryInterface import category_interface
from interfeces.filterInterface import filter_interfaces
from interfeces.transactionInterface import transaction_interface

def main_interface(account):

    transactions = features.all_transactions(account)
    categories = features.all_categories(account)

    tab_layout1 = [
        [sg.Push(),sg.Text("Movimientos de la cuenta", font=("Calibri", 18)),sg.Push()],
        [sg.Push(),sg.Table(values=transactions[0], headings=transactions[1], row_colors=transactions[2], key='-table_transactions-', justification = "center"),sg.Push()],
        [sg.Push(),sg.Button('Nuevo Gasto/Ingreso', key = 'button_new_transaction'),sg.Button('Filtrar', key = "button_filter"),sg.Button('Borrar Filtro', key = "button_clean_filter"),sg.Button('Estado de Cuenta', key = "button_account_statement"),sg.Push()],
        ]
    tab_layout2 = [
        [sg.Push(),sg.Text("Categorias Existentes", font=("Calibri", 18)),sg.Push(),],
        [sg.Push(),sg.Table(values=categories[0], headings=categories[1], row_colors=categories[2], key='table_categories', justification = "center", enable_events=True, expand_x=True,auto_size_columns = True),sg.Push()],
        [sg.Push(),sg.Button('Ingresar', key = 'button_new_category'),sg.Button('Modificar',key = 'button_category_modify'),sg.Push()],
        ]

    layout = [[sg.TabGroup([[sg.Tab("Transacciones en la Cuenta", tab_layout1), sg.Tab("Administrar Categorias", tab_layout2)]])]]
    window = sg.Window(f'Gestor de Finanzas de {account.name}', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break


        #tab_layout1 --> Movimientos de la cuenta

        elif event == 'button_new_transaction':
            if len(categories[0]) == 0:
                sg.popup('Debe crear una categoria primero')
                continue
            window.disable()
            account = transaction_interface(account)
            transactions = features.all_transactions(account)
            window['-table_transactions-'].update(values=transactions[0], row_colors=transactions[2])
            window.enable()

        elif event == 'button_filter':
            window.disable()
            filter_to_apply = filter_interfaces(account)
            transactions = features.filter_transactions (account, filter_to_apply)
            window['-table_transactions-'].update(values=transactions[0], row_colors=transactions[2])
            window.enable()
        
        elif event == "button_clean_filter":
            transactions = features.all_transactions(account)
            window['-table_transactions-'].update(values=transactions[0], row_colors=transactions[2])
        
        elif event == "button_account_statement":
            persistence.account_statement(account)
            sg.popup('Estado de Cuenta creado')

        #tab_layout2 --> "Categorias Existentes"

        elif event == 'table_categories':
            selected_row_indices = values['table_categories']
            if len(selected_row_indices) > 1:
                sg.popup('Solo puede seleccionar uno')
                window['table_categories'].update(select_rows=[])
                window['button_category_modify'].update(text=f"Modificar")
            else:
                for selected in selected_row_indices:
                    window['button_category_modify'].update(text=f"Modificar {categories[0][selected][0]}")

        elif event == 'button_new_category':
            window.disable()
            window['button_category_modify'].update(text=f"Modificar")
            account = category_interface(account)
            categories = features.all_categories(account)
            window['table_categories'].update(values=categories[0], row_colors=categories[2])
            window.enable()

        elif event == 'button_category_modify':
            selected_row_indices = values['table_categories']
            if len(selected_row_indices) == 0:
                sg.popup('Debe seleccionar una categería para modificarla')
            else:
                window.disable()
                window['button_category_modify'].update(text=f"Modificar")
                account = category_interface(account,categories[0][selected_row_indices[0]][0])
                categories = features.all_categories(account)
                window['table_categories'].update(values=categories[0], row_colors=categories[2])
                transactions = features.all_transactions(account)
                window['-table_transactions-'].update(values=transactions[0], row_colors=transactions[2])
                window.enable()

    window.close()
    return account