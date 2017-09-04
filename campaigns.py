import config
from launch import Launcher
import requests
import json

class Campaign(Launcher):
    def __init__(self):
        statusper().__init__()


    def add(self, name, list_to_send, launch_date = '2017-12-31 01:00'):
        action_name = 'campaign_create'
        self.params['api_action'] = action_name

        d = {
                'type': 'single'
                , 'name': name
                , 'sdate': launch_date # campaign send out timestamp
                , 'status': '1' # 0 = draft, 1 = scheduled 
                , 'public': '0' # 0 = not visible to public, 1 = visible
                , 'tracklinks': 'all' # track all links in bod
                , 'p[{}]'.format(list_to_send): list_to_send
                , 'm[1]': '100' # send message #1 to 100% of contacts
                }            

        return requests.post(
            self.api_url
            , params= self.params
            , headers= self.headers
            , data= d
            )

    def delete(self, id):
        action_name = 'campaign_delete'
        self.params['api_action'] = action_name

        return requests.get(
            self.api_url
            , params= {**self.params, **{'id':id}}
            , headers= self.headers
            )

    def list(self):
        action_name = 'campaign_list'
        self.params['api_action'] = action_name

        return requests.get(
            self.api_url
            , params= {**self.params, **{'ids':'all'}}
            , headers= self.headers
            )

        