import PySimpleGUI as sg
import ui_controller
import logic_controller

def screeningsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Book or Purchase Ticket':
        print("Pruchase Ticket!")
    if event == '-List-':
        sg.popup('{}'.format(values['-List-'][0]))


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

