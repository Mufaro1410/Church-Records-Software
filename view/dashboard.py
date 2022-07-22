from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "dashboard.kv"))

class DashboardMainWindow(MDScreen):
    pass

class DashboardWindow(MDBoxLayout):
    def switch_screen(self, screen_name, transition):
        self.ids.dashboard_screen_manager.transition.direction = transition
        self.ids.dashboard_screen_manager.current = screen_name

class DashboardApp(MDApp):
    def build(self):
        return DashboardWindow()

if __name__ == "__main__":
    DashboardApp().run()