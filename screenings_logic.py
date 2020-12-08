import PySimpleGUI as sg
import ui_controller
import logic_controller

def screeningsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Book Ticket':
        try:
            movie = values['-List-'][0]
            bookTicket(movie)
        except:
            sg.popup("Select a movie first")
    if event == 'Purchase Ticket':
        try:
            movie = values['-List-'][0]
            purchaseTicket(movie)
        except:
            sg.popup("Select a movie first")
    if event == '-List-':
        sg.popup('{}'.format(values['-List-'][0]))


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")


def bookTicket(movie):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_book_ticket_ui(movie)
    logic_controller.logic.set_book_ticket_user_loop()
    logic_controller.logic.set_auth_type("user")

def purchaseTicket(movie):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_purchase_ticket_ui(movie)
    logic_controller.logic.set_purchase_ticket_user_loop()
    logic_controller.logic.set_auth_type("user")

