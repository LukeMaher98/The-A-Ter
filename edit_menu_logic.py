import PySimpleGUI as sg
import logic_controller
import ui_controller
import ui_utils

def eventLoop(window, event, values):
    file = "databases/screenings_db.txt"

    if event == 'Main Menu':
        backToMenu()
    if event == 'Save':
        ui_utils.save_to_file(file, window['-MOVIES-'].get_list_values())
        sg.popup("Saved Screenings")
    if event == 'Add Screening':
        text = sg.popup_get_text("Add screening in format 'MovieTitle, Time1, Time2,..., TimeN")
        v = window['-MOVIES-'].get_list_values()
        v.append(convertToDisplayForm(text))
        window['-MOVIES-'].update(values=v)
        print(window['-MOVIES-'].get_list_values())
    if event == 'Delete Selected':
        print("DeleteSelected")
        d = values['-MOVIES-'][0]
        v = deleteSelected(d, window['-MOVIES-'].get_list_values())
        window['-MOVIES-'].update(values=v)
    if event == '-MOVIES-':
        text = sg.popup_get_text("Edit screening in format 'MovieTitle, Time1, Time2,..., TimeN",
            default_text=convertToEditForm(values['-MOVIES-'][0]))
        i = window['-MOVIES-'].get_indexes()
        v = window['-MOVIES-'].get_list_values()
        v[i[0]] = convertToDisplayForm(text)
        window['-MOVIES-'].update(values=v)

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()
    logic_controller.logic.set_auth_type("admin")

def convertToEditForm(input):
    output = input.split(':\t')[0]
    t = input.replace(output+":", "")
    output = output + "," + t.replace("\t", "")

    return output

def convertToDisplayForm(input):
    elements = input.split(",")
    count = 0
    output = ""
    for element in elements:
        if count == 0 :
            output += element + ":"
        else :
            output += "\t"+ element +","
        count +=1
    output = output.removesuffix(',')

    return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output
