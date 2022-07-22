from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "view/main.kv"))

from view import dashboard, login, members, services, sections, extras

class HomeWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.dashboard_screen.add_widget(dashboard.DashboardWindow())
        self.ids.members_screen.add_widget(members.MembersWindow())
        self.ids.services_screen.add_widget(services.ServicesWindow())
        self.ids.extras_screen.add_widget(extras.ExtrasWindow())
        #self.ids.sections_screen.add_widget(sections.SectionsWindow())

class MainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.login_screen.add_widget(login.LoginWindow())
        self.ids.home_screen.add_widget(HomeWindow())

    def switch_screen(self, screen_name, transition):
        self.ids.main_screen_manager.transition.direction = transition
        self.ids.main_screen_manager.current = screen_name

class MainApp(MDApp):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    MainApp().run()