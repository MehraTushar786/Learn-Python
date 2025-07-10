from engine import ChatBot
from utils import log_conversation

bot = ChatBot()
bot.greet()
while True:
    user = input("You: ")
    if(user.lower() == 'exit'):
        print('Bot: Bye!')
        break
    botRes = bot.respond(user)
    print(f"Bot:{botRes}")

    log_conversation(user,botRes)