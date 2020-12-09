import PySimpleGUI as sg
import entry_ui
import main_menu_ui
import edit_menu_ui
import screenings_ui
import concessions_ui
import ticket_sales_ui
import concession_sales_ui

class UI_Controller:
    def __init__(self): 
        self._login_ui = sg.Window(entry_ui.loginHeading, entry_ui.loginLayout, finalize=True) 
        self._signup_ui = None 
        self._main_menu_admin_ui = None 
        self._main_menu_user_ui = None
        self._edit_menu_ui = None
        self._screenings_ui = None
        self._concessions_ui = None
        self._ticket_sales_ui = None
        self._concession_sales_ui = None
        self._current_ui = self._login_ui  

    def open_login_ui(self):
        self._current_ui = self._login_ui

    def open_signup_ui(self):
        if self._signup_ui == None:
            self._signup_ui = sg.Window(entry_ui.signupHeading, entry_ui.signupLayout, finalize=True)
        self._current_ui = self._signup_ui

    def open_main_menu_admin_ui(self):
        if self._main_menu_admin_ui == None:
            self._main_menu_admin_ui = sg.Window(main_menu_ui.adminHeading, main_menu_ui.adminLayout, finalize=True)
        self._current_ui = self._main_menu_admin_ui

    def open_main_menu_user_ui(self):
        if self._main_menu_user_ui == None:
            self._main_menu_user_ui = sg.Window(main_menu_ui.userHeading, main_menu_ui.userLayout, finalize=True)
        self._current_ui = self._main_menu_user_ui
    
    def open_screening_ui(self):
        if self._screenings_ui == None:
            self._screenings_ui = sg.Window(screenings_ui.Heading, screenings_ui.userLayout,size=(600,200), finalize=True)
        self._current_ui = self._screenings_ui

    def open_concessions_ui(self):
        if self._concessions_ui == None:
            self._concessions_ui = sg.Window(concessions_ui.Heading, concessions_ui.userLayout,size=(600,250), finalize=True)
        self._current_ui = self._concessions_ui
    
    def open_ticket_sales_ui(self):
        if self._ticket_sales_ui == None:
            self._ticket_sales_ui = sg.Window(ticket_sales_ui.Heading, ticket_sales_ui.adminLayout,size=(600,200), finalize=True)
        self._current_ui = self._ticket_sales_ui

    def open_concession_sales_ui(self):
        if self._concession_sales_ui == None:
            self._concession_sales_ui = sg.Window(concession_sales_ui.Heading, concession_sales_ui.adminLayout,size=(600,200), finalize=True)
        self._current_ui = self._concession_sales_ui

    def open_edit_menu_ui(self):
        if self._edit_menu_ui == None:
            self._edit_menu_ui = sg.Window(edit_menu_ui.heading, edit_menu_ui.layout, finalize=True)
        self._current_ui = self._edit_menu_ui

    def get_current_ui(self):
        return self._current_ui

ui = UI_Controller()