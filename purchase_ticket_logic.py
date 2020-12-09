import PySimpleGUI as sg
import ui_controller
import logic_controller
import utils

def purchaseTicketLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Back To Screenings':
        screenings()
    if event == 'Purchase Ticket':
        try:
            title, time = utils.title_times_split(values['-List-'][0], False)
            sg.popup('Ticket purchased for: {} at {}'.format(title, time[0]))
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