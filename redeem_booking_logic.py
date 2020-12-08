import PySimpleGUI as sg
import ui_controller
import logic_controller
import ui_utils

def redeemBookingLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Redeem Booking':
        title, time = ui_utils.title_times_split(values['-List-'][0], False)
        user = ui_controller.ui._current_user
        sg.popup('Ticket redeemed for: {} at {}'.format(title, time[0]))
        removeBooking(user, title, time[0])
        movie = values['-List-'][0]
        purchaseTicket(movie)

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")

def purchaseTicket(movie):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_purchase_ticket_ui(movie)
    logic_controller.logic.set_purchase_ticket_user_loop()
    logic_controller.logic.set_auth_type("user")

def removeBooking(user, title, time):
    bookings = ""
    with open("databases/bookings_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if user == string[0] and title == string[1] and time == string[2]:
                pass
            else: 
                bookings += string[0]+","+string[1]+","+string[2]+",\n"

    db = open("databases/bookings_db.txt", "w")
    db.write(bookings)