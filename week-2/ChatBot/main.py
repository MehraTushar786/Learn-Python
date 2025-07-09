from engine import ChatBot

bot = ChatBot()
bot.greet()
while True:
    user = input("You: ")
    if(user.lower() == 'exit'):
        print('Bot: Bye!')
        break
    print(f"Bot: {bot.respond(user)}")