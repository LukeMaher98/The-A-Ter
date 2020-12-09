import PySimpleGUI as sg
import ui_utils
from listings import ListFactory

Heading = "TheAter Screenings"
list_factory = ListFactory()
screeningList = list_factory.create_list("databases/screenings_db.txt")
screeningsInfo = screeningList.get_view_list(screeningList.filename)

screeningsInfo = ui_utils.get_view_list("databases/screenings_db.txt")

userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(screeningsInfo, size=(100, len(screeningsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Book or Purchase Ticket')],
             [sg.Button('Back To Menu')]]