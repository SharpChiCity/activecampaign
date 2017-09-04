import config
from launch import Launcher
import requests


class Contact(Launcher):
    def __init__(self):
        super().__init__()


    def add(self, email, list_id=1, **kwargs):
        action_name = 'contact_add'
        self.params['api_action'] = action_name

        d = {'email': email
            , 'p[{}]'.format(list_id): list_id}
            
        for k in kwargs:
            d[k] = kwargs[k]

        return requests.post(
            self.api_url
            , params= self.params
            , headers= self.headers
            , data= d
            )

    def delete(self, id):
        action_name = 'contact_delete'
        self.params['api_action'] = action_name

        return requests.get(
            self.api_url
            , params= {**self.params, **{'id':id}}
            , headers= self.headers
            )
