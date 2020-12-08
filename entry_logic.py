import logic_controller
import ui_controller
import requests

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
            requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "login": "failed",
            "Reason": "Other"
            })
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")

def adminLogin(username):
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
        "timestamp": "2017-11-19T20:00:00.00Z",
        "AdminLogin": True,
          })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    ui_controller.ui.set_current_user(username)
    logic_controller.logic.set_current_user(username)
    logic_controller.logic.set_main_menu_admin_loop()
    logic_controller.logic.set_auth_type("admin")

def userLogin(username):
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
        "timestamp": "2017-11-19T20:00:00.00Z",
        "UserLogin": True,
          })
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
            requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "timestamp": "2017-11-19T20:00:00.00Z",
            "login": "failed",
            "Reason": "Password Invalid"
            })
    else:
        window['-OUTPUT-'].update("Entered username is invalid")
        requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
        "timestamp": "2017-11-19T20:00:00.00Z",
        "login": "failed",
        "Reason": "Username Invalid"
          })