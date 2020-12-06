import entry_logic
import main_menu_logic
import edit_menu_logic

class Logic_Controller:
    def __init__(self): 
        self._entry_loop = entry_logic.eventLoop 
        self._main_menu_admin_loop = main_menu_logic.adminEventLoop 
        self._main_menu_user_loop = main_menu_logic.userEventLoop
        self._current_loop = self._entry_loop
        self._auth_type = None
        self._exit = False
        self._edit_menu_loop = edit_menu_logic.eventLoop

    def set_entry_loop(self):  
        self._current_loop = self._entry_loop

    def set_main_menu_admin_loop(self):
        self._current_loop = self._main_menu_admin_loop

    def set_main_menu_user_loop(self):
        self._current_loop = self._main_menu_user_loop

    def set_edit_menu_loop(self):
        self._current_loop = self._edit_menu_loop

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