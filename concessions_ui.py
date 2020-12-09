import PySimpleGUI as sg
import ui_utils
import listings

Heading = "TheAter Concessions"

concessions_info = ui_utils.get_view_list("concessions","databases/concessions_db.txt")

concessions_list = listings.list_factory.create_list("concession",concessions_info)
concession_screen = concessions_list.generate_list()

userLayout = [[sg.Text("TheAter Concessions")], 
             [sg.Listbox(concession_screen, size=(100, len(concession_screen)), key='-List-', enable_events=True)],
             [sg.Button('Purchase Concessions')],
             [sg.Button('Back To Menu')]]