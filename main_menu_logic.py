import ui_controller
import logic_controller

def adminEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Screenings':
        print("Screenings")
    if event == 'My Bookings':
        print("My Bookings")
    if event == 'Bookings Review':
        print("Bookings Screen")
    if event == 'Sales Review':
        print("Sales Screen")

def userEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Screenings':
        editMenu()
    if event == 'My Bookings':
        print("My Bookings")

def logout():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_entry_ui()
    logic_controller.logic.set_entry_loop()
    logic_controller.logic.set_auth_type(None)

def editMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_edit_menu_ui()
    logic_controller.logic.set_edit_menu_loop()