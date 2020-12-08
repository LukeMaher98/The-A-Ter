import PySimpleGUI as sg
import ui_controller
import logic_controller
import ui_utils

Heading = "TheAter Purchase Ticket"

def showLayout(movie):
    title, showTimes = ui_utils.title_times_split(movie, True)
    return [[sg.Text(title)], 
             [sg.Listbox(showTimes, size=(100, len(showTimes)), key='-List-', bind_return_key=True)],
             [sg.Button('Purchase Ticket')],
             [sg.Button('Back To Screenings')],
             [sg.Button('Back To Menu')]]