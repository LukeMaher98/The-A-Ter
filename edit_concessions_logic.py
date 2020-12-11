import PySimpleGUI as sg
import logic_controller
import ui_controller
import utils
import re

concessionSales = utils.get_list("databases/concession_sales_db.txt")

def eventLoop(window, event, values):
    file = "databases/concessions_db.txt"

    if event == 'Main Menu':
        window['-CONCESSIONS-'].update(values=utils.get_view_list(file))
        backToMenu()
    if event == 'Save':
        utils.save_to_file(file, window['-CONCESSIONS-'].get_list_values())
        utils.save_list(file, concessionSales)
        sg.popup("Saved Concessions")
    if event == 'Add Concession':
        text = sg.popup_get_text("Add concession in format 'ConcessionName,Price'")
        if text != None:
            v = window['-CONCESSIONS-'].get_list_values() 
            m = convertToDisplayForm(text)
            v.append(m)
            concessionSales.append(appendToSales(text))
            print(concessionSales)
            window['-CONCESSIONS-'].update(values=v)
        else:
            sg.popup("Concessions must be in format 'ConcessionName,Price'")
    if event == 'Delete Selected':
        try:
            d = values['-CONCESSIONS-'][0]
            v = deleteSelected(d, window['-CONCESSIONS-'].get_list_values())
            window['-CONCESSIONS-'].update(values=v)
        except:
            sg.popup("Select concession to be deleted first!") 
    if event == '-CONCESSIONS-':
        text = sg.popup_get_text("Edit concession in format 'ConcessionName,Price'",
            default_text=convertToEditForm(values['-CONCESSIONS-'][0]))
        if text != None:
            i = window['-CONCESSIONS-'].get_indexes()
            j = getMatchingIndex(values['-CONCESSIONS-'][0], concessionSales)
            v = window['-CONCESSIONS-'].get_list_values()
            try:
                m = convertToDisplayForm(text)
                v[i[0]] = m
                concessionSales[j] = editSales(text, concessionSales[j])
                window['-CONCESSIONS-'].update(values=v)
            except:
                return
        else:
            sg.popup("Concessions must be in format 'ConcessionName,Price'")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

def convertToEditForm(input):
    element = input.split(":")
    output = element[0] + ","
    element[1] = element[1].replace(" ", "")
    output = output + element[1].removesuffix("e,\n")

    return output

def convertToDisplayForm(input):
    element = input.split(",")
    output = element[0] + ":"
    if re.match("[0-9]+", element[1]):
        output += "  "+ element[1] + "e,\n"
        return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output

def appendToSales(input):
    v = input.split(",")
    
    return(v[0]+",0,\n")

def editSales(new, old):
    n = new.split(",")
    o = old.split(",")

    output = n[0] + "," + o[1] + "," + o[2]
    return output

def getMatchingIndex(item, list):
    counter = 0
    i = item.split(":")
    for l in list:
        t = l.split(",")
        print(t[0] + " " + i[0])
        if t[0] == i[0]:
            return counter 
            print(counter)
        counter = counter + 1
