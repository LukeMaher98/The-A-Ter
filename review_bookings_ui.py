import PySimpleGUI as sg
import ui_controller
import logic_controller
import ui_utils

Heading = "TheAter My Bookings"

def showLayout():
    bookingsInfo = ui_utils.read_bookings_review()
    
    return [[sg.Text("Bookings Review")], 
             [sg.Listbox(bookingsInfo, size=(100, len(bookingsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]