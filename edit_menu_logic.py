import logic_controller
import ui_controller
import os

def eventLoop(window, event, values):
    file = "movie_db.txt"

    if event == 'Main Menu':
        print("Exit")
        backToMenu()
    if event == 'Save':
        WriteFile(file, values['-MOVIES-'][0])
    window.refresh()

def WriteFile(file, movies):
    f = open(file, "w")  
    for m in movies:
        f.write(m)
    f.close()

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()
    logic_controller.logic.set_auth_type("admin")