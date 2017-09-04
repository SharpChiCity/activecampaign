import config
import json
from launch import Launcher
import requests


class List(Launcher):
    def __init__(self):
        super().__init__()


    def add(self, list_name, sender_info):
        action_name = 'list_add'
        self.params['api_action'] = action_name

        return requests.post(
            self.api_url
            , params= self.params
            , headers= self.headers
            , data= {**{'name':list_name}, **sender_info}
            )

    def delete(self, id):
        action_name = 'list_delete'
        self.params['api_action'] = action_name

        return requests.get(
            self.api_url
            , params= {**self.params, **{'id':id}}
            , headers= self.headers
            )

    def list(self):
        action_name = 'list_list'
        self.params['api_action'] = action_name

        return requests.get(
            self.api_url
            , params= {**self.params, **{'ids':'all'}}
            , headers= self.headers
            )

    def delete_all(self):
        action_name = 'list_delete'
        self.params['api_action'] = action_name

        for id_nbr in json.loads(self.list().text):
            if id_nbr.isdigit():
                resp = self.delete(id_nbr)
                print(json.loads(resp.text))

# l = List()
# d = {
#        'sender_name': 'Kevin C',
#        'sender_addr1': 'my address',
#        'sender_city': 'Chicago',
#        'sender_zip': '123445',
#        'sender_country': 'USA'
#     }
# l.delete_all()
