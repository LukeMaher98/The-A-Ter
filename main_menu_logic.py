from review_bookings_logic import reviewBookingLoop
import ui_controller
import logic_controller
import requests

def adminEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Alter Screenings':
        print("Alter Screenings")
    if event == 'Bookings Review':
        reviewBookings()
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
        myBookings()

def logout():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_entry_ui()
    logic_controller.logic.set_entry_loop()
    logic_controller.logic.set_auth_type(None)

def screenings():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "screenings": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()
    logic_controller.logic.set_auth_type("user")


def concessions():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "concessions": True
            })

    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concessions_ui()
    logic_controller.logic.set_concessions_user_loop()
    logic_controller.logic.set_auth_type("user")

def myBookings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_redeem_booking_ui()
    logic_controller.logic.set_redeem_booking_user_loop()
    logic_controller.logic.set_auth_type("user")

def ticketSales():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "ticketsales": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_ticket_sales_ui()
    logic_controller.logic.set_ticket_sales_admin_loop()
    logic_controller.logic.set_auth_type("admin")
    

def concessionSales():
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "concessionsales": True
            })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concession_sales_ui()
    logic_controller.logic.set_concession_sales_admin_loop()
    logic_controller.logic.set_auth_type("admin")

def reviewBookings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_review_bookings_loop()
    logic_controller.logic.set_review_booking_loop()
    logic_controller.logic.set_auth_type("admin")
