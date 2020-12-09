import ui_controller
import logic_controller
import requests

def adminEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Alter Screenings':
        editMenu()
    if event == 'Bookings Review':
        print("Bookings Screen")
    if event == 'View Ticket Sales':
        ticketSales()
    if event == 'View Concession Sales':
        concessionSales()

def userEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Screenings':
        screenings()
    if event == 'Concessions':
        concessions()
    if event == 'My Bookings':
        print("My Bookings")

def logout():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_login_ui()
    logic_controller.logic.set_login_loop()
    logic_controller.logic.set_auth_type(None)

def editMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_edit_menu_ui()
    logic_controller.logic.set_edit_menu_loop()
    
def screenings():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "screenings": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()


def concessions():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "concessions": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concessions_ui()
    logic_controller.logic.set_concessions_user_loop()
    
def ticketSales():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "ticketsales": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_ticket_sales_ui()
    logic_controller.logic.set_ticket_sales_admin_loop()
    

def concessionSales():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "concessionsales": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concession_sales_ui()
    logic_controller.logic.set_concession_sales_admin_loop()
