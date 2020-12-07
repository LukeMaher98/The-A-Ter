import PySimpleGUI as sg
import ui_utils
Heading = "TheAter Ticket Sales"

ticketSalesInfo = ui_utils.get_view_list("databases/ticket_sales_db.txt")

adminLayout = [[sg.Text("TheAter Ticket Sales")], 
             [sg.Listbox(ticketSalesInfo, size=(100, len(ticketSalesInfo)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]