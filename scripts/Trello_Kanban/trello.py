import requests
import pprint as pp
import json
import os

class Trello():
    def __init__(self):
        
        self.base_url = "https://api.trello.com/1"
        self.url_dict = {
            "boards_url": "{}/members/me/boards".format(self.base_url),
            "get_board_url": "{}/boards".format(self.base_url),
            "get_card_url": "{}".format(self.base_url)
        }
        
        self.params_key_and_token = {
            'key':os.environ["TRELLO_API_KEY"],
            'token': os.environ["TRELLO_API_TOKEN"]}
    
