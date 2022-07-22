from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.network.urlrequest import UrlRequest

from kivy.lang import Builder

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "services.kv"))

class EditServicesWindow(MDScreen):
    services_url = 'http://127.0.0.1:8000/services/'

    def update_service(self):
        s_id = self.ids.id
        s_date = self.ids.date
        s_preacher = self.ids.preacher
        s_litegist_one = self.ids.litegist_one
        s_litegist_two = self.ids.litegist_two
        s_choir = self.ids.choir
        s_preaching_topic = self.ids.preaching_topic
        s_preaching_verses = self.ids.preaching_verses

        id = s_id.text
        date = s_date.text
        preacher = s_preacher.text
        litegist_one = s_litegist_one.text
        litegist_two = s_litegist_two.text
        choir = s_choir.text
        preaching_topic = s_preaching_topic.text
        preaching_verses = s_preaching_verses.text

        s_id.text = ''
        s_date.text = ''
        s_preacher.text = ''
        s_litegist_one.text = ''
        s_litegist_two.text = ''
        s_choir.text = ''
        s_preaching_topic.text = ''
        s_preaching_verses.text = ''

        updated_service = {"date": date, "preacher": preacher, "litegist_one": litegist_one, "litegist_two": litegist_two,
            "choir": choir, "preaching_topic": preaching_topic, "preaching_verses": preaching_verses}
        updated_service_json = json.dumps(updated_service)

        url = f'{self.services_url}{id}'
        UrlRequest(url, req_body=updated_service_json, method='PUT', on_success=self.service_updated)

    def service_updated(self, req, result):
        preaching_topic = result['preaching_topic']
        self.parent.parent.switch_screen("Services Screen", "right")
        Snackbar(text = f'{preaching_topic} Service Updated').open()

    def delete_service_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete service?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_service),
            ],
        )
        self.dialog.open()

    def delete_service(self, *args):
        s_id = self.ids.id
        id = s_id.text
        s_id.text = ''

        url = f'{self.services_url}{id}'
        UrlRequest(url, method='DELETE', on_success=self.service_deleted)
    
    def service_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Service Screen", "right")
        Snackbar(text = f'Service Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddServicesWindow(MDScreen):
    sections_url = 'http://127.0.0.1:8000/sections/'

    def create_service(self):
        s_id = self.ids.id
        s_date = self.ids.date
        s_preacher = self.ids.preacher
        s_litegist_one = self.ids.litegist_one
        s_litegist_two = self.ids.litegist_two
        s_choir = self.ids.choir
        s_preaching_topic = self.ids.preaching_topic
        s_preaching_verses = self.ids.preaching_verses

        id = s_id.text
        date = s_date.text
        preacher = s_preacher.text
        litegist_one = s_litegist_one.text
        litegist_two = s_litegist_two.text
        choir = s_choir.text
        preaching_topic = s_preaching_topic.text
        preaching_verses = s_preaching_verses.text

        s_id.text = ''
        s_date.text = ''
        s_preacher.text = ''
        s_litegist_one.text = ''
        s_litegist_two.text = ''
        s_choir.text = ''
        s_preaching_topic.text = ''
        s_preaching_verses.text = ''

        new_service = {"date": date, "preacher": preacher, "litegist_one": litegist_one, "litegist_two": litegist_two,
            "choir": choir, "preaching_topic": preaching_topic, "preaching_verses": preaching_verses}
        new_service_json = json.dumps(new_service)
        UrlRequest(self.sections_url, req_body=new_service_json, on_success=self.service_created)

    def service_created(self, req, result):
        preaching_topic = result['preaching_topic']
        #self.parent.parent.switch_screen("Services Screen", "right")
        Snackbar(text = f'{preaching_topic} Service Created').open()

class ServicesMainWindow(MDScreen):
    '''class for setting a searchable list of services on services home screen'''
    services_url = 'http://127.0.0.1:8000/services/'
    data = []

    def __init__(self, **kw):
        super().__init__(**kw)
        UrlRequest(self.services_url, on_success=self.get_services)
    
    def get_services(self, request, result):
        '''loop through the dic to get the id name of the service
            and append the selected data/dictionary to the global data list'''
        for i in result:
            services_dict = {}
            services_dict['id'] = str(i['id'])
            services_dict['preaching_topic'] = i['preaching_topic']
            services_dict['date'] = i['date']
            self.data.append(services_dict)
        self.set_search_services()

    def set_search_services(self, text="", search=False):
        '''function that creates a seachable list and 
            append list items to the services main screen'''

        def add_service_item(name):
            self.ids.services_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_service(x),
                }
            )
        self.ids.services_list.data = []
        for item in self.data:
            id = item['id']
            preaching_topic = item['preaching_topic']
            date = item['date']
            name = f'{id} - "{preaching_topic} {date}'
            if search:
                if text in name:
                    add_service_item(name)
            else:
                add_service_item(name)

    def edit_service(self, name):
        '''function for searching a particular service in database'''
        id = name[0]
        url = f'{self.services_url}{id}'
        UrlRequest(url, on_success=self.edit_service_screen)

    def edit_service_screen(self, request, result):
        '''function that opens and displays service information on edit screen'''
        self.parent.get_screen("Edit Services Screen").ids.id.text = str(result['id'])
        self.parent.get_screen("Edit Services Screen").ids.date.text = result['date']
        self.parent.get_screen("Edit Services Screen").ids.preacher.text = result['preacher']
        self.parent.get_screen("Edit Services Screen").ids.litegist_one.text = result['litegist_one']
        self.parent.get_screen("Edit Services Screen").ids.litegist_two.text = result['litegist_two']
        self.parent.get_screen("Edit Services Screen").ids.choir.text = result['choir']
        self.parent.get_screen("Edit Services Screen").ids.preaching_topic.text = result['preaching_topic']
        self.parent.get_screen("Edit Services Screen").ids.preaching_verses.text = result['preaching_verses']

        self.parent.parent.switch_screen("Edit Services Screen", "left")

class ServicesWindow(MDBoxLayout):
    def switch_screen(self, screen_name, transition):
        self.ids.services_screen_manager.transition.direction = transition
        self.ids.services_screen_manager.current = screen_name

class ServicesApp(MDApp):
    def build(self):
        return ServicesWindow()

if __name__ == "__main__":
    ServicesApp().run()