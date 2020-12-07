import ui_controller
import logic_controller

def adminEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Alter Screenings':
        print("Alter Screenings")
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
    ui_controller.ui.open_entry_ui()
    logic_controller.logic.set_entry_loop()
    logic_controller.logic.set_auth_type(None)

def screenings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()
    logic_controller.logic.set_auth_type("user")

def concessions():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concessions_ui()
    logic_controller.logic.set_concessions_user_loop()
    logic_controller.logic.set_auth_type("user")

def ticketSales():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_ticket_sales_ui()
    logic_controller.logic.set_ticket_sales_admin_loop()
    logic_controller.logic.set_auth_type("admin")

def concessionSales():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concession_sales_ui()
    logic_controller.logic.set_concession_sales_admin_loop()
    logic_controller.logic.set_auth_type("admin")