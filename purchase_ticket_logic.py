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
            addSale(title)
            backToMenu()
        except:
            sg.popup("Select a time first")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")

def screenings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()
    logic_controller.logic.set_auth_type("user")

def addSale(title):
    ticketSales = ""
    with open("databases/ticket_sales_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if title == string[0]:
                ticketSales += title+","+str(int(string[1]) + 1)+",\n"
            else:
                ticketSales += line

    db = open("databases/ticket_sales_db.txt", "w")
    db.write(ticketSales)