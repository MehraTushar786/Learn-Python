import os

def log_conversation(user,bot):
    currDir = os.path.dirname(__file__)
    filePath = os.path.join(currDir,'chat_log.txt')

    with open(filePath,'a',encoding='utf-8') as f:
        f.write(f"User: {user}\n")
        f.write(f"bot: {bot}\n")