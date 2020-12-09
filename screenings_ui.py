import PySimpleGUI as sg
import utils

Heading = "TheAter Screenings"

screeningsInfo = utils.get_view_list("databases/screenings_db.txt")

userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(screeningsInfo, size=(100, len(screeningsInfo)), key='-List-', bind_return_key=True)],
             [sg.Button('Book Ticket')],
             [sg.Button('Purchase Ticket')],
             [sg.Button('Back To Menu')]]