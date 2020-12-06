import PySimpleGUI as sg
import entry_ui
import main_menu_ui
import edit_menu_ui

class UI_Controller:
    def __init__(self): 
        self._entry_ui = sg.Window(entry_ui.heading, entry_ui.layout, finalize=True) 
        self._main_menu_admin_ui = None 
        self._main_menu_user_ui = None
        self._edit_menu_ui = None
        self._current_ui = self._entry_ui  

    def open_entry_ui(self):
        self._current_ui = self._entry_ui

    def open_main_menu_admin_ui(self):
        if self._main_menu_admin_ui == None:
            self._main_menu_admin_ui = sg.Window(main_menu_ui.adminHeading, main_menu_ui.adminLayout, finalize=True)
        self._current_ui = self._main_menu_admin_ui

    def open_main_menu_user_ui(self):
        if self._main_menu_user_ui == None:
            self._main_menu_user_ui = sg.Window(main_menu_ui.userHeading, main_menu_ui.userLayout, finalize=True)
        self._current_ui = self._main_menu_user_ui

    def open_edit_menu_ui(self):
        if self._edit_menu_ui == None:
            self._edit_menu_ui = sg.Window(edit_menu_ui.heading, edit_menu_ui.layout, finalize=True)
        self._current_ui = self._edit_menu_ui

    def get_current_ui(self):
        return self._current_ui

ui = UI_Controller()