from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "membership.kv"))

class EditMembershipWindow(MDScreen):
    membership_url = 'http://127.0.0.1:8000/membership/'

    def update_membership(self):
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

        url = f'{self.membership_url}{id}'
        updated_section = {"sections_number": sections_number, "area": area, "section_leader": section_leader, "vice_section_leader": vice_section_leader,
            "treasurer": treasurer, "number_of_families": number_of_families}
        updated_section_json = json.dumps(updated_section)
        UrlRequest(url, req_body=updated_section_json, method='PUT', on_success=self.membership_updated)

    def membership_updated(self, req, result):
        section_name = result['section_name']
        self.parent.parent.switch_screen("Sections Screen", "right")
        Snackbar(text = f'{section_name} Updated').open()

    def delete_membership_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete section?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_membership),
            ],
        )
        self.dialog.open()

    def delete_membership(self, *args):
        s_id = self.ids.id
        id = s_id.text
        s_id.text = ''

        url = f'{self.sections_url}{id}'
        UrlRequest(url, method='DELETE', on_success=self.membership_deleted)
    
    def membership_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Sections Screen", "right")
        Snackbar(text = f'Section Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddMembershipWindow(MDScreen):
    membership_url = 'http://127.0.0.1:8000/membership/'

    def create_membership(self):
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
        UrlRequest(self.membership_url, req_body=new_section_json, on_success=self.membership_created)

    def membership_created(self, req, result):
        section_number = result['section_number']
        #self.parent.parent.switch_screen("Sections Screen", "right")
        Snackbar(text = f'Secton {section_number} Created').open()

class MembershipMainWindow(MDScreen):
    '''class for setting a searchable list of sections on sections home screen'''
    membership_url = 'http://127.0.0.1:8000/membership/'
    data = []

    def __init__(self, **kw):
        super().__init__(**kw)
        UrlRequest(self.membership_url, on_success=self.get_sections)
    
    def get_sections(self, request, result):
        '''loop through the dic to get the id name of the section
            and append the selected data/dictionary to the global data list'''
        for i in result:
            sections_dict = {}
            sections_dict['id'] = str(i['id'])
            sections_dict['section_number'] = i['section_number']
            self.data.append(sections_dict)
        self.set_search_sections()

    def set_search_sections(self, text="", search=False):
        '''function that creates a seachable list and 
            append list items to the sections main screen'''

        def add_section_item(name):
            self.ids.sections_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_section(x),
                }
            )
        self.ids.sections_list.data = []
        for item in self.data:
            id = item['id']
            section_number = item['section_number']
            name = f'{id} - "Section "+{section_number}'
            if search:
                if text in name:
                    add_section_item(name)
            else:
                add_section_item(name)

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

class MembershipWindow(MDScreen):
    membership_screen_manager = ObjectProperty()

    def switch_screen(self, screen_name, transition):
        self.membership_screen_manager.transition.direction = transition
        self.membership_screen_manager.current = screen_name

class MembershipApp(MDApp):
    def build(self):
        return MembershipWindow()

if __name__ == "__main__":
    MembershipApp().run()