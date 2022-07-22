from cgitb import text
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json
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
    sections_url = 'http://127.0.0.1:8000/sections/'

    def update_section(self):
        s_id = self.ids.id
        s_number = self.ids.section_number
        s_area = self.ids.area
        s_section_leader = self.ids.section_leader
        s_vice_section_leader = self.ids.vice_section_leader
        s_treasurer = self.ids.treasurer
        s_number_of_families = self.ids.number_of_families

        id = s_id.text
        sections_number = s_number.text
        area = s_area.text
        section_leader = s_section_leader.text
        vice_section_leader = s_vice_section_leader.text
        treasurer = s_treasurer.text
        number_of_families = s_number_of_families.text

        s_id.text = ''
        s_number.text = ''
        s_area.text = ''
        s_section_leader.text = ''
        s_vice_section_leader.text = ''
        s_treasurer.text = ''
        s_number_of_families.text = ''

        url = f'{self.sections_url}{id}'
        updated_section = {"sections_number": sections_number, "area": area, "section_leader": section_leader, "vice_section_leader": vice_section_leader,
            "treasurer": treasurer, "number_of_families": number_of_families}
        updated_section_json = json.dumps(updated_section)
        UrlRequest(url, req_body=updated_section_json, method='PUT', on_success=self.section_updated)

    def section_updated(self, req, result):
        section_name = result['section_name']
        self.parent.parent.switch_screen("Sections Screen", "right")
        Snackbar(text = f'{section_name} Updated').open()

    def delete_section_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete section?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_section),
            ],
        )
        self.dialog.open()

    def delete_section(self, *args):
        s_id = self.ids.id
        id = s_id.text
        s_id.text = ''

        url = f'{self.sections_url}{id}'
        UrlRequest(url, method='DELETE', on_success=self.section_deleted)
    
    def section_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Sections Screen", "right")
        Snackbar(text = f'Section Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddSectionsWindow(MDScreen):
    sections_url = 'http://127.0.0.1:8000/sections/'

    def create_section(self):
        #s_id = self.ids.id
        s_number = self.ids.section_number
        s_area = self.ids.area
        s_section_leader = self.ids.section_leader
        s_vice_section_leader = self.ids.vice_section_leader
        s_treasurer = self.ids.treasurer
        s_number_of_families = self.ids.number_of_families

        #id = s_id.text
        sections_number = s_number.text
        area = s_area.text
        section_leader = s_section_leader.text
        vice_section_leader = s_vice_section_leader.text
        treasurer = s_treasurer.text
        number_of_families = s_number_of_families.text

        #s_id.text = ''
        s_number.text = ''
        s_area.text = ''
        s_section_leader.text = ''
        s_vice_section_leader.text = ''
        s_treasurer.text = ''
        s_number_of_families.text = ''

        new_section = {"sections_number": sections_number, "area": area, "section_leader": section_leader, "vice_section_leader": vice_section_leader,
            "treasurer": treasurer, "number_of_families": number_of_families}
        new_section_json = json.dumps(new_section)
        UrlRequest(self.sections_url, req_body=new_section_json, on_success=self.section_created)

    def section_created(self, req, result):
        section_number = result['section_number']
        #self.parent.parent.switch_screen("Sections Screen", "right")
        Snackbar(text = f'Secton {section_number} Created').open()

class ExtrasMainWindow(MDScreen):
    sections_url = 'http://127.0.0.1:8000/sections/'
    # memberStatus_url = 'http://127.0.0.1:8000/memberstatus/'
    # membership_url = 'http://127.0.0.1:8000/membership/'
    # maritalStatus_url = 'http://127.0.0.1:8000/marital/'
    # users_url = 'http://127.0.0.1:8000/users/'

    data = []

    def __init__(self, **kw):
        super().__init__(**kw)
        UrlRequest(self.sections_url, on_success=self.getSections)
        # UrlRequest(self.memberStatus_url, on_success=self.getMemberStatus)
        # UrlRequest(self.membership_url, on_success=self.getMemberships)
        # UrlRequest(self.maritalStatus_url, on_success=self.getMaritalStatus)
        # UrlRequest(self.users_url, on_success=self.getUsers)
    
    def getSections(self, request, result):
        '''loop through the dic to get the id name of the section
            and append the selected data/dictionary to the global data list'''
        for i in range(1,17):
            self.ids.sections_list.add_widget(OneLineListItem(text=f'Section {i}'))

    def edit_section(self, name):
        '''function for searching a particular section in database'''
        id = name[0]
        url = f'{self.sections_url}{id}'
        UrlRequest(url, on_success=self.edit_section_screen)

    def edit_section_screen(self, request, result):
        '''function that opens and displays section information on edit screen'''
        self.parent.get_screen("Edit Sections Screen").ids.id.text = str(result['id'])
        self.parent.get_screen("Edit Sections Screen").ids.section_number.text = result['section_number']
        self.parent.get_screen("Edit Sections Screen").ids.area.text = result['area']
        self.parent.get_screen("Edit Sections Screen").ids.section_leader.text = result['section_leader']
        self.parent.get_screen("Edit Sections Screen").ids.vice_section_leader.text = result['vice_section_leader']
        self.parent.get_screen("Edit Sections Screen").ids.treasurer.text = result['treasurer']
        self.parent.get_screen("Edit Sections Screen").ids.number_of_families.text = result['number_of_families']
        self.parent.parent.switch_screen("Edit Sections Screen", "left")

class ExtrasWindow(MDBoxLayout):
    def switch_screen(self, screen_name, transition):
        self.ids.extras_screen_manager.transition.direction = transition
        self.ids.extras_screen_manager.current = screen_name

class ExtrasApp(MDApp):
    def build(self):
        return ExtrasWindow()

if __name__ == "__main__":
    ExtrasApp().run()