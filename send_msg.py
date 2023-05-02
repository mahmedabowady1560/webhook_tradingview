import os
from telegram import Bot

def sendMessage(data):
    tg_bot = Bot(token=os.environ['TOKEN'])
    channel = os.environ['CHANNEL']
    try:
        tg_bot.send_message(
            channel ,
            data ,
            parse_mode="MARKDOWN"


        )
        return True
    except KeyError:
        tg_bot.send_message(
            channel,
            data,
            parse_Mode="MARKDWON"
        )
    except Exception as e :
        print("[X] Telgram Error :\n>",e)
    return False