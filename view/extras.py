from cgitb import text
from logging import root
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDFlatButton, MDRaisedButton
# from kivymd.uix.list import OneLineListItem
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.snackbar import Snackbar

from kivy.properties import ObjectProperty
# from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "extras.kv"))

from view.extra import sections, membership, memberStatus, maritalStatus, users

# class SectionsWindow(MDScreen):
#     pass

class ExtrasMainWindow(MDScreen):
    pass

class ExtrasWindow(MDScreen):
    extras_screen_manager = ObjectProperty()

    def __init__(self, **kw):
        super(ExtrasWindow, self).__init__(**kw)

        self.extras_screen_manager.add_widget(sections.SectionsWindow())
        self.extras_screen_manager.add_widget(membership.MembershipWindow())
        self.extras_screen_manager.add_widget(memberStatus.MemberStatusWindow())
        self.extras_screen_manager.add_widget(maritalStatus.MaritalStatusWindow())
        self.extras_screen_manager.add_widget(users.UsersWindow())

    def switch_screen(self, screen_name, transition):
        self.extras_screen_manager.transition.direction = transition
        self.extras_screen_manager.current = screen_name

class ExtrasApp(MDApp):
    def build(self):
        return ExtrasWindow()

if __name__ == "__main__":
    ExtrasApp().run()