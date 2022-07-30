from turtle import Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ObjectProperty

# from kivy.lang import Builder

# import os

# dirname = os.path.dirname(__file__)

# Builder.load_file(os.path.join(dirname, "view/main.kv"))

from view import dashboard, login, members, services, extras

class ContentNavigationDrawer(MDBoxLayout):
    pass

class HomeWindow(MDScreen):
    home_screen_manager = ObjectProperty()
    home_nav_drawer = ObjectProperty()

class MainWindow(MDBoxLayout):
    home_window = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.ids.login_screen.add_widget(login.LoginWindow())
        self.home_window.home_screen_manager.add_widget(dashboard.DashboardMainWindow())
        self.home_window.home_screen_manager.add_widget(members.MembersWindow())
        self.home_window.home_screen_manager.add_widget(services.ServicesWindow())
        self.home_window.home_screen_manager.add_widget(extras.ExtrasWindow())

    def switch_screen(self, screen_name, transition):
        self.home_window.home_screen_manager.transition.direction = transition
        self.home_window.home_screen_manager.current = screen_name
        self.home_window.home_nav_drawer.set_state('close')


class MainApp(MDApp):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    MainApp().run()