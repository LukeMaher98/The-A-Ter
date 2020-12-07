import PySimpleGUI as sg
import view_controller

Heading = "TheAter Screenings"

screeningsInfo = view_controller.view.get_view_list("databases/screenings_db.txt")

userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(screeningsInfo, size=(100, len(screeningsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Book or Purchase Ticket')],
             [sg.Button('Back To Menu')]]