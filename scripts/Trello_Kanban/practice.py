import requests
import pprint as pp
import json
import os

#Trello docs
#https://developers.trello.com/reference/#introduction

api_key = os.environ["TRELLO_API_KEY"]
api_token = os.environ["TRELLO_API_TOKEN"]

base_url = "https://api.trello.com/1"
url = '{}/members/me/boards'.format(base_url)

#Fun fact: Trello API depends on authorization via params, not headers
params_key_and_token = {'key':api_key,'token':api_token}
arguments = {'fields': 'name', 'lists': 'open'}

response = requests.get(url=url, params=params_key_and_token, data=arguments)

pp.pprint(json.loads(response.text))