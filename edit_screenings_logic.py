import PySimpleGUI as sg
import logic_controller
import ui_controller
import re
import utils
import listings

def eventLoop(window, event, values):
    file = "databases/screenings_db.txt"
    if event == 'Main Menu':
        screenings_info = utils.get_view_list("movies",file)
        movie_list = listings.list_factory.create_list("movie",screenings_info)
        movie_screen = movie_list.generate_list()
        window['-MOVIES-'].update(values=movie_screen)
        backToMenu()
    if event == 'Save':
        movies = window['-MOVIES-'].get_list_values()
        s = []
        for m in movies:
            s.append(convertToSaveForm(m)+"\n")
        utils.save_list(file, s)
        sg.popup("Saved Screenings")
    if event == 'Add Screening':
        text = sg.popup_get_text("Add screening in format 'MovieTitle,Screen,Time1,...,TimeN")
        if text != None:
            v = window['-MOVIES-'].get_list_values()
            m = convertToDisplayForm(text)
            if m.endswith(":  ") != True:
                v.append(m)
                window['-MOVIES-'].update(values=v)
            else:
                sg.popup("Screenings must be in format 'MovieTitle,Screen,Time1,...,TimeN")
    if event == 'Delete Selected':
        try:
            d = values['-MOVIES-'][0]
            v = deleteSelected(d, window['-MOVIES-'].get_list_values())
            window['-MOVIES-'].update(values=v)
        except:
            sg.popup("Select Screening to be deleted first!") 
    if event == '-MOVIES-':
        text = sg.popup_get_text("Edit screening in format 'MovieTitle,Screen,Time1,...,TimeN",
            default_text=convertToEditForm(values['-MOVIES-'][0]))
        if text != None:
            i = window['-MOVIES-'].get_indexes()
            v = window['-MOVIES-'].get_list_values()
            m = convertToDisplayForm(text)
            if m.endswith(":") != True:
                v[i[0]] = m
                window['-MOVIES-'].update(values=v)
            else:
                sg.popup("Screenings must be in format 'MovieTitle,Screen,Time1,...,TimeN")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

def convertToEditForm(input):
    o = input.split(' -')[0]
    input = input.replace(o+" -  ", "")
    o = o.replace("Screen ", "")
    output = input.split(': ')[0]
    t = input.replace(output+":  ", "")
    output = output + "," + o + ","
    output = output + t.replace(" ", ",")
    output = output.removesuffix(",")

    return output

def convertToSaveForm(input):
    o = input.split(' -')[0]
    input = input.replace(o+" -  ", "")
    o = o.replace("Screen ", "")
    output = input.split(': ')[0]
    t = input.replace(output+": ", "")
    output = output + "," + o
    output = output + t.replace(" ", ", ")

    return output

def convertToDisplayForm(input):
    elements = input.split(",")
    count = 0
    output = ""
    t = ""
    for element in elements:
        if count == 0 : 
            t = element + ":  "
        elif count == 1:
            if re.match("[0-9][0-9]|[0-9]", element):
                output = "Screen " + element + " -  " + t
        else:
            if re.match("(2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])", element):
                output += element + " "
        count += 1

    return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output
