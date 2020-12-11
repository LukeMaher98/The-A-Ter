import PySimpleGUI as sg
import utils

concessionInfo = utils.get_view_list("databases/concessions_db.txt")
print(concessionInfo)

layout = [[sg.Text('Double click or press Enter on selected concession to edit')],
            [sg.Listbox(concessionInfo, size=(100, len(concessionInfo)), key='-CONCESSIONS-', bind_return_key=True)],
            [sg.Button('Save'), sg.Button('Add Concession'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Concessions"