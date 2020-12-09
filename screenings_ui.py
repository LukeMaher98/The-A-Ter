import PySimpleGUI as sg
import utils

Heading = "TheAter Screenings"

screeningsInfo = utils.get_view_list("databases/screenings_db.txt")

userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(screeningsInfo, size=(100, len(screeningsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Book or Purchase Ticket')],
             [sg.Button('Back To Menu')]]