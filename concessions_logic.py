import PySimpleGUI as sg
import ui_controller
import logic_controller

def concessionsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Purchase Concessions':
        try:
            error_check = values['-List-'][0]
            concession = values['-List-']
            purchaseConcession(concession)
        except:
            sg.popup("Select a concession first")
    if event == '-List-':
        sg.popup('{} euro'.format(values['-List-'][0]))


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")

def purchaseConcession(concession):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_purchase_concessions_loop(concession)
    logic_controller.logic.set_purchase_concession_loop()
    logic_controller.logic.set_auth_type("user")
