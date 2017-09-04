import config
from launch import Launcher
import requests


class Address(Launcher):
    def __init__(self):
        super().__init__()


    def add(self, name, list_id):
        action_name = 'address_add'
        self.params['api_action'] = action_name

        d = {
            'company_name': name
            , 'address_1': 'my address'
            , 'city': 'Chicago'
            , 'state': 'Illinois'
            , 'zip': '90210'
            , 'country': 'USA'
            , 'list[{}]'.format(list_id): list_id
            }

        return requests.post(
            self.api_url
            , params= self.params
            , headers= self.headers
            , data= d
            )
