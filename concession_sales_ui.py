import PySimpleGUI as sg
import ui_utils

Heading = "TheAter Concession Sales"

concessionSalesInfo = ui_utils.get_view_list("databases/concession_sales_db.txt")

adminLayout = [[sg.Text("TheAter Concession Sales")], 
             [sg.Listbox(concessionSalesInfo, size=(100, len(concessionSalesInfo)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]