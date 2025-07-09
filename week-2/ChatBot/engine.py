
import os
class ChatBot():
    def __init__(self):
        self.responses = {
            "hi": "Hello! 👋",
            "how are you": "I'm just a bunch of Python code, but doing great!",
            "bye": "Goodbye! Have a great day!",
            "help": "I can respond to: hi, how are you, bye, help"
        }

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