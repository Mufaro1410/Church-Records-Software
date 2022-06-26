from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "extras.kv"))

class EditUsersWindow(MDScreen):
    pass

class AddUsersWindow(MDScreen):
    pass

class EditMaritalStatusWindow(MDScreen):
    pass

class AddMaritalStatusWindow(MDScreen):
    pass

class MembershipWindow(MDScreen):
    pass

class EditMembershipWindow(MDScreen):
    pass

class AddMembershipWindow(MDScreen):
    pass

class EditMemberStatusWindow(MDScreen):
    pass

class AddMemberStatusWindow(MDScreen):
    pass

class EditSectionsWindow(MDScreen):
    pass

class AddSectionsWindow(MDScreen):
    pass

class ExtrasMainWindow(MDScreen):
    pass

class ExtrasWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(1, 20):
            self.ids.extras_screen_manager.get_screen('Extras Home').ids.sections_list.add_widget(OneLineIconListItem(text=f'Section {i}'))
        for i in ["Full Member", "Probationer"]:
            self.ids.extras_screen_manager.get_screen('Extras Home').ids.member_status_list.add_widget(OneLineIconListItem(text=i))
        for i in ["MUMC", "RRW", "UMYF", "INFANTS", "PASTORIAL"]:
            self.ids.extras_screen_manager.get_screen('Extras Home').ids.membership_list.add_widget(OneLineIconListItem(text=i))
        for i in ["Married", "Single", "Widow", "Widower"]:
            self.ids.extras_screen_manager.get_screen('Extras Home').ids.marital_status_list.add_widget(OneLineIconListItem(text=i))
        for i in range(1, 20):
            self.ids.extras_screen_manager.get_screen('Extras Home').ids.users_list.add_widget(OneLineIconListItem(text=f'User {i}'))

    def switch_screen(self, screen_name, transition):
        self.ids.extras_screen_manager.transition.direction = transition
        self.ids.extras_screen_manager.current = screen_name

class ExtrasApp(MDApp):
    def build(self):
        return ExtrasWindow()

if __name__ == "__main__":
    ExtrasApp().run()