import PySimpleGUI as sg
import view_controller

movieInfo = view_controller.view.get_view_list("movie_db.txt")

layout = [[sg.Listbox(movieInfo, key='-MOVIES-')],
          [sg.Button('Save'), sg.Button('Main Menu')]]

heading = "Edit Screenings"