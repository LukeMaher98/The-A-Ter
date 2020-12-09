import PySimpleGUI as sg
import utils
import logic_controller

Heading = "TheAter Concessions"

concessionsInfo = utils.get_view_list("databases/concessions_db.txt")
concessionsBasket = logic_controller.logic.get_concessions_basket()

# userLayout = [[sg.Text("TheAter Concessions")], 
#              [sg.Listbox(concessionsInfo, size=(100, len(concessionsInfo)), key='-List-', bind_return_key=True)],
#              [sg.Button('Purchase Concessions')],
#              [sg.Button('Back To Menu')]]
userLayout = [[sg.Text("TheAter Concessions")],
              [sg.Listbox(concessionsInfo, size=(50, 8), key='-LIST-', enable_events=True),
               sg.Listbox(concessionsBasket, size=(50, 8), key='-BASKET-', enable_events=True)],
              [sg.Button('Purchase Concessions')],
              [sg.Button('Back To Menu')]]
