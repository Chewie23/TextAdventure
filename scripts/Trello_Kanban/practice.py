import requests
import pprint as pp
import json
import os

#Trello docs
#https://developers.trello.com/reference/#introduction

api_key = os.environ["TRELLO_API_KEY"]
api_token = os.environ["TRELLO_API_TOKEN"]

base_url = "https://api.trello.com/1"
boards_url = '{}/members/me/boards'.format(base_url)

#Fun fact: Trello API depends on authorization via params, not headers
params_key_and_token = {'key': api_key,'token': api_token}
arguments = {'fields': 'name', 'lists': 'open'}

response = requests.get(url=boards_url, params=params_key_and_token, data=arguments)

boards_response = json.loads(response.text)

for board in boards_response:
    if "StarFinder: Task tracking" in board["name"]:
        board_id = board["id"]
        
specific_board_url = "{}/boards/{}/cards".format(base_url, board_id)
response = requests.get(url=specific_board_url, params=params_key_and_token, data=arguments)

pp.pprint(json.loads(response.text))

