import FreeSimpleGUI as sg
from feature import features

def filter_interfaces(account):
    list_category = features.list_categories(account)
    filter_to_apply = {}

    layout = [
        [sg.Text("Filtrar", font=("Calibri", 18))],
        [sg.Text("Fecha Inicio:"), sg.Input(key='input_start_date',size=10),sg.CalendarButton(key="start_date_button",button_text='Seleccionar Fecha',format="%Y-%m-%d")],
        [sg.Text("Fecha Fin:"), sg.Input(key='input_end_date',size=10),sg.CalendarButton(key="end_date_button",button_text='Seleccionar Fecha',format="%Y-%m-%d")],
        [sg.Text("Categoria:"),sg.Combo(key ='input_category', values = list_category)], 
        [sg.Text("Tipo:"),sg.Combo(key ='input_type', values = ['Ingreso','Gasto'])], 
        [sg.Push(),sg.Button('Aceptar'),sg.Button('Cancelar'),sg.Push()],
        ]
    
    window = sg.Window('Ingresar Categoria', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break 
        
        elif event == "Aceptar":
            try: 
                filter_to_apply = features.check_filter(start_date= values['input_start_date'],end_date=values['input_end_date'],category=values['input_category'],type=values['input_type'])
                break
            
            except Exception as e:
                sg.popup(e)
                continue
    
    window.close()
    return filter_to_apply