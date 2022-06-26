from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "services.kv"))

class EditServicesWindow(MDScreen):
    pass

class AddServicesWindow(MDScreen):
    pass

class ServicesMainWindow(MDScreen):
    pass

class ServicesWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(1,21):
            self.ids.services_screen_manager.get_screen('Services Screen').ids.services_list.add_widget(OneLineAvatarListItem(text=f'Service {i}'))

    def switch_screen(self, screen_name, transition):
        self.ids.services_screen_manager.transition.direction = transition
        self.ids.services_screen_manager.current = screen_name

class ServicesApp(MDApp):
    def build(self):
        return ServicesWindow()

if __name__ == "__main__":
    ServicesApp().run()