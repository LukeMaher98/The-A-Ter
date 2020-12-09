import PySimpleGUI as sg
import ui_utils

movieInfo = ui_utils.get_view_list("databases/screenings_db.txt")

layout = [[sg.Text('Double click or press Enter on selected screening to edit')],
            [sg.Listbox(movieInfo, size=(100, len(movieInfo)), key='-MOVIES-', bind_return_key=True)],
            [sg.Button('Save'), sg.Button('Add Screening'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Screenings"