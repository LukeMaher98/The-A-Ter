import PySimpleGUI as sg
import ui_controller
import logic_controller

def concessionsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Purchase Concessions':
    #     try:
    #         error_check = values['-List-'][0]
    #         concession = values['-List-']
    #         purchaseConcession(concession)
    #     except:
    #         sg.popup("Select a concession first")
    # if event == '-List-':
    #     sg.popup('{} euro'.format(values['-List-'][0]))

        print(f'{"Subtotal: "}{logic_controller.logic.get_concessions_subtotal()}{"e"}')
    if event == '-LIST-':
        addToConcessionsBasket(window, values['-LIST-'][0])
    if event == '-BASKET-':
        removeFromConcessionsBasket(window, values['-BASKET-'][0])

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

def addToConcessionsBasket(window, value):
    concessions = logic_controller.logic.get_concessions_basket()
    concessions.append(value)
    logic_controller.logic.set_concessions_basket(concessions)
    subtotal = logic_controller.logic.get_concessions_subtotal()
    subtotal += parseItemPrice(value)
    logic_controller.logic.set_concessions_subtotal(subtotal)   
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

def removeFromConcessionsBasket(window, value):
    concessions = logic_controller.logic.get_concessions_basket()
    concessions.remove(value)
    logic_controller.logic.set_concessions_basket(concessions)
    subtotal = logic_controller.logic.get_concessions_subtotal()
    subtotal -= parseItemPrice(value)
    logic_controller.logic.set_concessions_subtotal(subtotal) 
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

def parseItemPrice(value):
    strPrice = value[value.rfind(":"): value.rfind("e")]
    strPrice = strPrice.replace(":", "")
    strPrice = strPrice = strPrice.replace(" ", "")
    return int(strPrice)




def purchaseConcession(concession):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_purchase_concessions_loop(concession)
    logic_controller.logic.set_purchase_concession_loop()
    logic_controller.logic.set_auth_type("user")
