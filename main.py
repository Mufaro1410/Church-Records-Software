from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

from view import login, members, services, extras

class HomeWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.members_screen.add_widget(members.MembersWindow())
        self.ids.services_screen.add_widget(services.ServicesWindow())
        self.ids.extras_screen.add_widget(extras.ExtrasWindow())
        #self.ids.users_screen.add_widget(users.UsersWindow())

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