from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, 'members.kv'))

class EditMembersWindow(MDScreen):
    pass

class AddMembersWindow(MDScreen):
    pass

class MembersMainWindow(MDScreen):
    pass

class MembersWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(1,21):
            self.ids.members_screen_manager.get_screen("Members Screen").ids.members_list.add_widget(OneLineAvatarListItem(text=f'Member {i}'))
    
    def switch_screen(self, screen_name, transition):
        self.ids.members_screen_manager.transition.direction = transition
        self.ids.members_screen_manager.current = screen_name

class MembersApp(MDApp):
    def build(self):
        return MembersWindow()

if __name__ == "__main__":
    MembersApp().run()