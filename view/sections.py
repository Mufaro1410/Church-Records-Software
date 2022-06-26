from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

class EditMembersWindow(MDBoxLayout):
    pass

class AddMembersWindow(MDBoxLayout):
    pass

class MembersMainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(1,21):
            self.ids.members_list.add_widget(OneLineAvatarListItem(text=f'Member {i}')) #divider='Inset'

class MembersWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.members_main_screen.add_widget(MembersMainWindow ())
        self.ids.add_members_screen.add_widget(AddMembersWindow())
        self.ids.edit_members_screen.add_widget(EditMembersWindow())

    def switch_screen(self, screen_name, transition):
        self.ids.members_screen_manager.transition.direction = transition
        self.ids.members_screen_manager.current = screen_name

class MembersApp(MDApp):
    def build(self):
        return MembersWindow()

if __name__ == "__main__":
    MembersApp().run()