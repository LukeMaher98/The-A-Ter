import PySimpleGUI as sg
import entry_ui
import main_menu_ui
import screenings_ui
import concessions_ui
import ticket_sales_ui
import concession_sales_ui
import book_ticket_ui
import purchase_ticket_ui
import redeem_booking_ui

class UI_Controller:
    def __init__(self): 
        self._entry_ui = sg.Window(entry_ui.heading, entry_ui.layout, finalize=True) 
        self._main_menu_admin_ui = None 
        self._main_menu_user_ui = None
        self._screenings_ui = None
        self._concessions_ui = None
        self._ticket_sales_ui = None
        self._concession_sales_ui = None
        self._book_ticket_ui = None
        self._purchase_ticket_ui = None
        self._redeem_booking_ui = None
        self._current_ui = self._entry_ui  
        self._current_user = None

    def open_entry_ui(self):
        self._current_ui = self._entry_ui

    def set_current_user(self, username):
        self._current_user = username

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
            self._screenings_ui = sg.Window(screenings_ui.Heading, screenings_ui.userLayout,size=(600,230), finalize=True)
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

    def open_book_ticket_ui(self, movie):
        # no if here as each movie has a different layout and it will need to be overwritten
        self._book_ticket_ui = sg.Window(book_ticket_ui.Heading, book_ticket_ui.showLayout(movie), size=(600,200), finalize=True)
        self._current_ui = self._book_ticket_ui

    def open_purchase_ticket_ui(self, movie):
        # no if here as each movie has a different layout and it will need to be overwritten
        self._purchase_ticket_ui = sg.Window(purchase_ticket_ui.Heading, purchase_ticket_ui.showLayout(movie), size=(600,200), finalize=True)
        self._current_ui = self._purchase_ticket_ui
    
    def open_redeem_booking_ui(self):
        # no if here as each movie has a different layout and it will need to be overwritten
        self._redeem_booking_ui = sg.Window(redeem_booking_ui.Heading, redeem_booking_ui.showLayout(), size=(600,200), finalize=True)
        self._current_ui = self._redeem_booking_ui

    def get_current_ui(self):
        return self._current_ui

ui = UI_Controller()