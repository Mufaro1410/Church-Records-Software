from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, 'members.kv'))

class EditMembersWindow(MDScreen):
    members_url = 'http://127.0.0.1:8000/members/'

    def update_member(self):
        m_id = self.ids.id
        f_name = self.ids.first_name
        m_surname = self.ids.surname
        m_dob = self.ids.date_of_birth
        m_contact = self.ids.contact_details
        m_address = self.ids.address
        m_marital_status_id = self.ids.marital_status_id
        m_member_status_id = self.ids.member_status_id
        m_membership_id = self.ids.membership_id
        m_section_id = self.ids.section_id

        id = m_id.text
        first_name = f_name.text
        surname = m_surname.text
        date_of_birth = m_dob.text
        contact = m_contact.text
        address = m_address.text
        marital_status_id = m_marital_status_id.text
        member_status_id = m_member_status_id.text
        membership_id = m_membership_id.text
        section_id = m_section_id.text

        m_id.text = ''
        f_name.text = ''
        m_surname.text = ''
        m_dob.text = ''
        m_contact.text = ''
        m_address.text = ''
        m_marital_status_id.text = ''
        m_member_status_id.text = ''
        m_membership_id.text = ''
        m_section_id.text = ''

        url = f'{self.members_url}{id}'
        updated_member = {"first_name": first_name, "surname": surname, "date_of_birth": date_of_birth, "contact": contact, "address": address,
            "marital_status_id": marital_status_id, "member_status_id": member_status_id, "membership_id": membership_id, "section_id": section_id}
        updated_member_json = json.dumps(updated_member)
        UrlRequest(url, req_body=updated_member_json, method='PUT', on_success=self.member_updated)

    def member_updated(self, req, result):
        first_name = result['first_name']
        surname = result['surname']
        self.parent.parent.switch_screen("Members Home Screen", "right")
        Snackbar(text = f'{first_name} {surname} Updated').open()

    def delete_member_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete member?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_member),
            ],
        )
        self.dialog.open()

    def delete_member(self, *args):
        m_id = self.ids.id
        id = m_id.text
        m_id.text = ''

        url = f'{self.members_url}{id}'
        UrlRequest(url, method='DELETE', on_success=self.member_deleted)
    
    def member_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Members Home Screen", "right")
        Snackbar(text = f'Member Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddMembersWindow(MDScreen):
    members_url = 'http://127.0.0.1:8000/members/'

    def create_member(self):
        #m_id = self.ids.id
        f_name = self.ids.first_name
        m_surname = self.ids.surname
        m_dob = self.ids.date_of_birth
        m_gender = self.ids.gender
        m_contact = self.ids.contact_details
        m_email = self.ids.email
        m_address = self.ids.address
        m_marital_status_id = self.ids.marital_status_id
        m_member_status_id = self.ids.member_status_id
        m_membership_id = self.ids.membership_id
        m_section_id = self.ids.section_id

        #id = m_id.text
        first_name = f_name.text
        surname = m_surname.text
        date_of_birth = m_dob.text
        gender = m_gender.text
        contact = m_contact.text
        email = m_email.text
        address = m_address.text
        marital_status_id = m_marital_status_id.text
        member_status_id = m_member_status_id.text
        membership_id = m_membership_id.text
        section_id = m_section_id.text

        #m_id.text = ''
        f_name.text = ''
        m_surname.text = ''
        m_dob.text = ''
        m_gender.text = ''
        m_contact.text = ''
        m_email.text = ''
        m_address.text = ''
        m_marital_status_id.text = ''
        m_member_status_id.text = ''
        m_membership_id.text = ''
        m_section_id.text = ''

        new_member = {"first_name": first_name, "surname": surname, "date_of_birth": date_of_birth, 'gender': gender, "contact": contact, 'email': email, 
            "address": address, "marital_status_id": marital_status_id, "member_status_id": member_status_id, "membership_id": membership_id, 
            "section_id": section_id}
        new_member_json = json.dumps(new_member)

        UrlRequest(self.members_url, req_body=new_member_json, on_success=self.member_created)

    def member_created(self, req, result):
        first_name = result['first_name']
        surname = result['surname']
        self.parent.parent.switch_screen("Members Screen", "right")
        Snackbar(text = f'{first_name} {surname}Created').open()

class MembersMainWindow(MDScreen):
    '''class for setting a searchable list of members on members home screen'''
    members_url = 'http://127.0.0.1:8000/members/'
    data = []

    def __init__(self, **kw):
        super().__init__(**kw)
        UrlRequest(self.members_url, on_success=self.get_members)
    
    def get_members(self, request, result):
        '''loop through the dic to get the id, first and last name of the member 
            and append the selected data/dictionary to the global data list'''
        for i in result:
            members_dict = {}
            members_dict['id'] = str(i['id'])
            members_dict['surname'] = i['surname']
            members_dict['first_name'] = i['first_name']
            self.data.append(members_dict)
        self.set_search_members()

    def set_search_members(self, text="", search=False):
        '''function that creates a seachable list and 
            append list items to the members main screen'''

        def add_member_item(name):
            self.ids.members_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_member(x),
                }
            )
        self.ids.members_list.data = []
        for item in self.data:
            id = item['id']
            first_name = item['first_name']
            surname = item['surname']
            name = f'{id} - {first_name} {surname}'
            if search:
                if text in name:
                    add_member_item(name)
            else:
                add_member_item(name)

    def edit_member(self, name):
        '''function for searching a particular member in database'''
        id = name[0]
        url = f'{self.members_url}{id}'
        UrlRequest(url, on_success=self.edit_customer_screen)

    def edit_customer_screen(self, request, result):
        '''function that opens and displays member information on edit screen'''
        self.parent.get_screen("Edit Members Screen").ids.id.text = str(result['id'])
        self.parent.get_screen("Edit Members Screen").ids.first_name.text = result['first_name']
        self.parent.get_screen("Edit Members Screen").ids.surname.text = result['surname']
        self.parent.get_screen("Edit Members Screen").ids.contact_details.text = result['contact']
        self.parent.get_screen("Edit Members Screen").ids.gender.text = result['gender']
        self.parent.get_screen("Edit Members Screen").ids.contact_details.text = result['contact']
        self.parent.get_screen("Edit Members Screen").ids.email.text = result['email']
        self.parent.get_screen("Edit Members Screen").ids.address.text = result['address']
        self.parent.get_screen("Edit Members Screen").ids.marital_status_id.text = str(result['marital_status_id'])
        self.parent.get_screen("Edit Members Screen").ids.member_status_id.text = str(result['member_status_id'])
        self.parent.get_screen("Edit Members Screen").ids.membership_id.text = str(result['membership_id'])
        self.parent.get_screen("Edit Members Screen").ids.section_id.text = str(result['section_id'])
        self.parent.parent.switch_screen("Edit Members Screen", "left")

class MembersWindow(MDScreen):

    def switch_screen(self, screen_name, transition):
        self.ids.members_screen_manager.transition.direction = transition
        self.ids.members_screen_manager.current = screen_name

class MembersApp(MDApp):
    def build(self):
        return MembersWindow()

if __name__ == "__main__":
    MembersApp().run()