from random import lognormvariate
import PySimpleGUI as sg
import ui_controller
import logic_controller
import ui_utils

Heading = "TheAter My Bookings"

def showLayout():
    bookingsInfo = ui_utils.read_bookings(logic_controller.logic._current_user)
    
    return [[sg.Text("My Bookings")], 
             [sg.Listbox(bookingsInfo, size=(100, len(bookingsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Redeem Booking')],
             [sg.Button('Back To Menu')]]