from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
#from kivymd.uix.screen import MDScreen

from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "login.kv"))

# LOGIN SCREEN
class LoginWindow(MDBoxLayout):
    def proceed(self):
        self.parent.parent.current = 'Home Screen'
    '''
    login_url = 'http://127.0.0.1:8000/login'
    token = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        uname = self.ids.username
        pword = self.ids.password
        self.info = self.ids.info

        username = uname.text
        password = pword.text

        uname.text = ''
        pword.text = ''

        login_details = {'username': username, 'password': password}
        login_details_json = json.dumps(login_details)

        UrlRequest(self.login_url, req_body=login_details_json, on_success=self.got_json, on_failure=self.invalid_credentials)

    def got_json(self, req, result):
        role = result['role']
        username = result['username']
        if role == 'Administrator':
            self.parent.parent.parent.ids.main_screen.children[0].ids.active_user.secondary_text = username
        #    self.parent.parent.parent.ids.home_screen.children[0].ids.register.children[0].active_user = username
        #    self.parent.parent.parent.ids.home_screen.children[0].ids.register.children[0].designation = role
        #    self.parent.parent.parent.ids.home_screen.children[0].ids.inventory_management.children[0].ids.receive_inventory_screen.children[0].active_user = username
            self.parent.parent.parent.ids.main_screen.children[0].ids.dashboard_list_item.disabled = False
            self.parent.parent.parent.ids.main_screen.children[0].ids.inventory_list_item.disabled = False
            self.parent.parent.parent.ids.main_screen.children[0].ids.users_list_item.disabled = False
            self.parent.parent.parent.ids.main_screen.children[0].ids.reports_list_item.disabled = False
            self.parent.parent.transition.direction = 'left'
            self.parent.parent.current = 'Main_Screen'
        else:
            self.parent.parent.parent.ids.main_screen.children[0].ids.active_user.secondary_text = username
            self.parent.parent.parent.ids.main_screen.children[0].ids.dashboard_list_item.disabled = True
            self.parent.parent.parent.ids.main_screen.children[0].ids.inventory_list_item.disabled = True
            self.parent.parent.parent.ids.main_screen.children[0].ids.users_list_item.disabled = True
            self.parent.parent.parent.ids.main_screen.children[0].ids.reports_list_item.disabled = True
            self.parent.parent.transition.direction = 'left'
            self.parent.parent.current = 'Main_Screen'

    def invalid_credentials(self, req, result):
        self.info.text = 'Invalid Credentials'

    def proceed(self):
        self.parent.parent.parent.ids.main_screen.children[0].ids.active_user.secondary_text = 'mufaro'
        #self.parent.parent.parent.ids.main_screen.children[0].ids.dashboard_list_item.disabled = True
        self.parent.parent.current = 'Main_Screen'
    '''

class LoginApp(MDApp):
    def build(self):
        return LoginWindow()

if __name__ == '__main__':
    LoginApp().run()