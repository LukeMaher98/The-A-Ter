import entry_logic
import main_menu_logic
import screenings_logic
import concessions_logic
import ticket_sales_logic
import concession_sales_logic
import book_ticket_logic
import purchase_ticket_logic
import redeem_booking_logic
import review_bookings_logic

class Logic_Controller:
    def __init__(self): 
        self._entry_loop = entry_logic.eventLoop 
        self._main_menu_admin_loop = main_menu_logic.adminEventLoop 
        self._main_menu_user_loop = main_menu_logic.userEventLoop
        self._screenings_user_loop = screenings_logic.screeningsEventLoop
        self._concessions_user_loop = concessions_logic.concessionsEventLoop
        self._ticket_sales_admin_loop = ticket_sales_logic.ticketSalesEventLoop
        self._concession_sales_admin_loop = concession_sales_logic.concessionSalesEventLoop
        self._book_ticket_user_loop = book_ticket_logic.bookTicketLoop
        self._purchase_ticket_user_loop = purchase_ticket_logic.purchaseTicketLoop
        self._redeem_booking_user_loop = redeem_booking_logic.redeemBookingLoop
        self._review_booking_loop = review_bookings_logic.reviewBookingLoop
        self._current_loop = self._entry_loop
        self._current_user = None
        self._auth_type = None
        self._exit = False

    def set_entry_loop(self):
        self._current_loop = self._entry_loop

    def set_current_user(self, username):
        self._current_user = username

    def set_main_menu_admin_loop(self):
        self._current_loop = self._main_menu_admin_loop

    def set_main_menu_user_loop(self):
        self._current_loop = self._main_menu_user_loop
    
    def set_screenings_user_loop(self):
        self._current_loop = self._screenings_user_loop
   
    def set_concessions_user_loop(self):
        self._current_loop = self._concessions_user_loop

    def set_ticket_sales_admin_loop(self):
        self._current_loop = self._ticket_sales_admin_loop

    def set_concession_sales_admin_loop(self):
        self._current_loop = self._concession_sales_admin_loop

    def set_book_ticket_user_loop(self):
        self._current_loop = self._book_ticket_user_loop

    def set_purchase_ticket_user_loop(self):
        self._current_loop = self._purchase_ticket_user_loop
    
    def set_redeem_booking_user_loop(self):
        self._current_loop = self._redeem_booking_user_loop

    def set_review_booking_loop(self):
        self._current_loop = self._review_booking_loop

    def get_current_loop(self):
        return self._current_loop

    def set_auth_type(self, auth_type):
        self._auth_type = auth_type

    def get_auth_type(self):
        return self._auth_type 

    def exit(self):
        self._exit = True 

    def get_exit(self):
        return self._exit 

logic = Logic_Controller()