import PySimpleGUI as sg
import ui_utils

Heading = "TheAter Concessions"

concessionsInfo = ui_utils.get_view_list("databases/concessions_db.txt")

userLayout = [[sg.Text("TheAter Concessions")], 
             [sg.Listbox(concessionsInfo, size=(100, len(concessionsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Purchase Concessions')],
             [sg.Button('Back To Menu')]]