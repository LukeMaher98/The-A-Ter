import logic_controller
import ui_controller

def eventLoop(window, event, values):
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")
    if event == 'Exit':
        logic_controller.logic.exit()
    if event == 'Confirm':
        if (values['-PASSWORD-'] != '') and (values['-USERNAME-'] != ''):
            validateLogin(window, values['-USERNAME-'], values['-PASSWORD-'])
        else:
            window['-OUTPUT-'].update("Invalid details entered")
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")

def adminLogin(username):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    ui_controller.ui.set_current_user(username)
    logic_controller.logic.set_current_user(username)
    logic_controller.logic.set_main_menu_admin_loop()
    logic_controller.logic.set_auth_type("admin")

def userLogin(username):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    ui_controller.ui.set_current_user(username)
    logic_controller.logic.set_current_user(username)
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")

def validateLogin(window, username, password):
    loginData = open("databases/login_db.txt", "r")
    usernames = loginData.readline().split(",")
    passwords = loginData.readline().split(",")
    authTypes = loginData.readline().split(",")
    if username in usernames:
        if password == passwords[usernames.index(username)]:
            if authTypes[usernames.index(username)] == "admin":
                adminLogin(username)
            else:
                userLogin(username)
        else:
            window['-OUTPUT-'].update("Entered password is invalid")
    else:
        window['-OUTPUT-'].update("Entered username is invalid")