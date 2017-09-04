import config

class Launcher:
    def __init__(self):
        self.api_url = config.api_url
        self.api_token = config.api_token
        self.headers = {'Content-Type':'application/x-www-form-urlencoded'}

        self.params = {'api_key': self.api_token
                    , 'api_output': 'json'
                    # , 'api_action': ''
                }
