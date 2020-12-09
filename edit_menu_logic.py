import PySimpleGUI as sg
import logic_controller
import ui_controller
import re
import utils

def eventLoop(window, event, values):
    file = "databases/screenings_db.txt"

    if event == 'Main Menu':
        window['-MOVIES-'].update(values=utils.get_view_list("screening",file))
        backToMenu()
    if event == 'Save':
        utils.save_to_file(file, window['-MOVIES-'].get_list_values())
        sg.popup("Saved Screenings")
    if event == 'Add Screening':
        text = sg.popup_get_text("Add screening in format 'MovieTitle,Time1,Time2,...,TimeN")
        if text != None:
            v = window['-MOVIES-'].get_list_values()
            m = convertToDisplayForm(text)
            if m.endswith(":") != True:
                v.append(m)
                window['-MOVIES-'].update(values=v)
            else:
                sg.popup("Screenings must be in format 'MovieTitle,Time1,Time2,...,TimeN")
    if event == 'Delete Selected':
        try:
            d = values['-MOVIES-'][0]
            v = deleteSelected(d, window['-MOVIES-'].get_list_values())
            window['-MOVIES-'].update(values=v)
        except:
            sg.popup("Select Screening to be deleted first!") 
    if event == '-MOVIES-':
        text = sg.popup_get_text("Edit screening in format 'MovieTitle,Time1,Time2,...,TimeN",
            default_text=convertToEditForm(values['-MOVIES-'][0]))
        if text != None:
            i = window['-MOVIES-'].get_indexes()
            v = window['-MOVIES-'].get_list_values()
            m = convertToDisplayForm(text)
            if m.endswith(":") != True:
                v[i[0]] = m
                window['-MOVIES-'].update(values=v)
            else:
                sg.popup("Screenings must be in format 'MovieTitle,Time1,Time2,...,TimeN")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

def convertToEditForm(input):
    output = input.split(':  ')[0]
    t = input.replace(output+":", "")
    output = output + "," + t.replace("  ", "")

    return output

def convertToDisplayForm(input):
    elements = input.split(",")
    count = 0
    output = ""
    for element in elements:
        if count == 0 :
            output += element + ":"
        else :
            if re.match("(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])", element):
                output += "  "+ element +","
        count +=1
    output = output.removesuffix(',')

    return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output
