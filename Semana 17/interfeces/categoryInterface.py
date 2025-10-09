import FreeSimpleGUI as sg
from feature.objects import Category
from feature import persistence, features

def category_interface(account, category_name=None):
    
    selected_category = None
    category_modify = False
    name_color = None
    if category_name:
        categories = account.categories
        for category in categories:
            if category.category == category_name:
                name_color = category.color
                selected_category = category
                category_modify = True


    layout = [
        [sg.Text("Ingresar Categoria", font=("Calibri", 18))],
        [sg.Text("Nombre:"), sg.Input(key='input_category_name', default_text = category_name)],
        [sg.Text("Color:"), sg.Input(key='input_category_color',default_text=name_color),sg.ColorChooserButton(key="color_button",button_text='Seleccionar Color', default_color=name_color)],
        [sg.Button('Aceptar'),sg.Button('Cancelar')],
        ]
    
    window = sg.Window('Ingresar Categoria', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        
        elif event == "color_button":
            window["color_button"].update(default_color = values['category_color'])
        
        elif event == "Aceptar":
            try:
                if category_modify:
                    selected_category = features.modify_category(selected_category, category_name=values['input_category_name'],category_color=values['input_category_color'])
                    sg.popup('Categoria Modificada')
                else:
                    account = features.new_category(account, category_name=values['input_category_name'],category_color=values['input_category_color'])
                    sg.popup('Categoria Agregada')
                persistence.save_account(account)
                break
            except Exception as e:
                sg.popup(e)
                continue
    
    window.close()
    return account


