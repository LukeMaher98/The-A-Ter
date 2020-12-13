import PySimpleGUI as sg
import ui_controller
import logic_controller
from utils import utils
import requests

def purchaseTicketLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Back To Screenings':
        screenings()
    if event == 'Purchase Ticket':
        try:
            title, time = utils.title_times_split(values['-List-'][0], False)
            sg.popup('Ticket purchased for: {} at {}'.format(title, time[0]))
            requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "PurchaseTicket": "Success",
        })
            backToMenu()
        except:
            sg.popup("Select a time first")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

def screenings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()