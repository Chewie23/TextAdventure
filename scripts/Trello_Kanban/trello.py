import requests
import pprint as pp
import json
import os

#TODO
#Abstract away the request boilerplate of key and token

class Trello():
    """
    The Trello class. Will be used to automate the boring stuff
    such as creating a checklist of cards or managing the board (i.e. shifting
    from one list to another)
    """
    def __init__(self):
        
        self.base_url = "https://api.trello.com/1"
        self.url_dict = {
            "boards_url": "{}/members/me/boards".format(self.base_url),
            "get_board_url": "{}/boards".format(self.base_url),
            "get_card_url": "{}".format(self.base_url)
        }
        
        self.params_key_and_token = {
            'key': os.environ["TRELLO_API_KEY"],
            'token': os.environ["TRELLO_API_TOKEN"]}
            
        self.arguments = {'fields': 'name', 'lists': 'open'}
    
    def get_boards(self):
        """
        Gets all the boards information associated with the
        member's account
        """
        response = requests.get(
            url=self.url_dict["boards_url"], 
            params=self.params_key_and_token, 
            data=self.arguments
        )

        return json.loads(response.text)

if __name__ == "__main__":
    trello = Trello()
    
    pp.pprint(trello.get_boards())
        
