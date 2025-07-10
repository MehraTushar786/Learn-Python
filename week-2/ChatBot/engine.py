
import os
import json
class ChatBot():
    def __init__(self):
        currDif = os.path.dirname(__file__)
        filePath =  os.path.join(currDif,'./response.json')
        try:
            with open(filePath,'r') as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            print('No response.txt file Found in the Directory')
            self.responses = {}



    def greet(self):
        currDir = os.path.dirname(__file__)
        filePath =  os.path.join(currDir,'./greet.txt')
        with open(filePath,'r') as f:
            content = f.read()
            print(content)

    def respond(self,user_input):
        user_input = user_input.lower()
        data = self.responses.get(user_input)
        if(data is None):
            return "I'm not sure how to respond to that 🤔"
        
        return data