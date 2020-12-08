import PySimpleGUI as sg
import ui_controller
import logic_controller
import ui_utils

def purchaseConcessionLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Back to Concessions':
        backToConcessions()
    if event == 'Purchase Concession':
        proceed = True
        concession = ""
        try:
            concession = values['-List-'][0]
        except:
            proceed = False
            sg.popup("Select a concession first")
        if proceed:
            amount = sg.popup_get_text("Select Amount")
            try:
                amount = int(amount)
                if amount > 0:
                    buyConcession(concession, amount)
                    backToMenu()
                else:
                    sg.popup("Select a value greater than 0")
            except:
                sg.popup("Select a numeric value")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")

def backToConcessions():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concessions_ui()
    logic_controller.logic.set_concessions_user_loop()
    logic_controller.logic.set_auth_type("user")

def buyConcession(concession, amount):
    concessionSales = ""
    concession = concession[:concession.index(":")]
    with open("databases/concession_sales_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if concession == string[0]:
                concessionSales += concession+","+str(int(string[1]) + amount)+",\n"
            else:
                concessionSales += line

    db = open("databases/concession_sales_db.txt", "w")
    db.write(concessionSales)