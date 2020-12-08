import PySimpleGUI as sg
import ui_controller
import logic_controller
import ui_utils

Heading = "TheAter Purchase Concession"

def showLayout(concession):
    return [[sg.Text("Purchase Concession")], 
             [sg.Listbox(concession, size=(100, len(concession)), key='-List-', bind_return_key=True)],
             [sg.Button('Purchase Concession')],
             [sg.Button('Back to Concessions')],
             [sg.Button('Back To Menu')]]