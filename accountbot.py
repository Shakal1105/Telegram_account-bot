from pyrogram import Client, filters
import random
from time import sleep

class Automess():
    def __init__(self):
        self.anima=0
        self.a=0
        self.start=True
        self.api_id = 9958356
        self.api_hash = "8895b2a2b674f00658660440ef8adcbb"
        self.admins = [697798016]
        self.key = {}
        # Конфиг
        self.privetstvie = ['hi','hello','hey','пр',"привет","доров","здрасте","приветик","ку"]
        self.otvet = ["Hi","Приветик","Ку","Привет"]
        self.prefix = ["+", "-", "^-^"]

        self.word = filters.text
        self.start = True

        self.app()

        ################################################################3

    def app(self):
        user = Client('Automessage', self.api_id, self.api_hash)

        user.start()

        user.stop()

        print('run')

        @user.on_message(filters.command('members'.lower(), prefixes=self.prefix) & filters.me)
        def info_key(user, message):
            user.send_message(message.chat.id, "{}".format(self.key))
        
        @user.on_message(filters.command('surprise'.lower(), prefixes=self.prefix) & filters.me)
        def surprise(user, message):
        	message_id=message.message_id
        	sleep(0.9)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                     Хуй\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡\n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                      Хуй\n                    Стояв\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡ \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                      Хуй\n                    Стояв\n                       Та\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                      Хуй\n                    Стояв\n                       Та\n                    Серце \n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡  \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                      Хуй\n                    Стояв\n                       Та\n                    Серце \n                   Билось\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡ \n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                      Хуй\n                    Стояв\n                       Та\n                    Серце \n                   Билось\n                     🎉💐\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(0.2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢᠎⁣⁢‌⁠⁢⁣᠎⁢‌⁡\n          🧡🧡🧡          🧡🧡🧡\n            🧡🧡🧡      🧡🧡🧡\n               🧡🧡🧡🧡🧡🧡\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n  ❤️❤️❤️❤️🧡🧡🧡❤️❤️❤️❤️\n\n\n\n                     Щоб\n                      Хуй\n                    Стояв\n                       Та\n                    Серце \n                   Билось\n                     🎉💐\n                      🥳\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️\n       ❤️❤️❤️🧡🧡🧡❤️❤️❤️")
        	sleep(2)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="Хэппи Пёздэй!! \nот \n Shakal and LPar!")
        
        @user.on_message(filters.command('void'.lower(), prefixes=self.prefix) & filters.me)
        def pystota(user, message):
        	user.delete_messages(message.chat.id, message.message_id)
        	user.send_message(message.chat.id, "⁢⁣⁡⁢‍᠎⁡⁣⁠⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣ ")
        
        @user.on_message(filters.command('hearths'.lower(), prefixes=self.prefix) & filters.me)
        def serdechko(user, message):
            self.start=True
            tim=0
            message_id=message.message_id
            while self.start:
            	tim+=1
            	user.edit_message_text(message.chat.id,message_id=message_id,text="⁡﻿‌\n⁡﻿‌\n\n      \n   \n     \n              💧💧            💧💧 \n            💧💧💧       💧💧💧\n             💧 💧 💧 💧 💧 💧\n               💧💧💧💧💧💧 \n                  💧 💧 💧 💧 \n                     💧 💧 💧 \n                        💧 💧\n                           💧 \n                 \n                      \n                         ⁡﻿‌")
            	sleep(0.5)
            	user.edit_message_text(message.chat.id,message_id=message_id,text="⁡﻿‌\n\n\n         \n     \n           🩸🩸🩸        🩸🩸🩸\n        🩸 💧💧🩸  🩸💧💧 🩸\n       🩸💧💧💧 🩸 💧💧💧🩸\n        🩸💧 💧 💧 💧 💧 💧🩸\n          🩸💧💧💧💧💧💧 🩸\n            🩸 💧 💧 💧 💧 🩸\n               🩸 💧 💧 💧 🩸\n                  🩸 💧 💧 🩸 \n                     🩸💧 🩸 \n                          🩸  \n                     \n                         ⁡﻿‌")
            	sleep(0.5)
            	user.edit_message_text(message.chat.id,message_id=message_id,text="⁡﻿‌\n⁡﻿‌\n\n           💧💧💧        💧💧💧\n         💧💧💧💧   💧💧💧💧\n      💧🩸🩸🩸  💧 🩸🩸🩸💧\n   💧🩸 💧💧🩸  🩸💧💧 🩸💧\n  💧🩸💧💧💧 🩸 💧💧💧🩸💧\n   💧🩸💧 💧 💧 💧 💧 💧🩸💧\n     💧🩸💧💧💧💧💧💧 🩸💧\n       💧🩸 💧 💧 💧 💧 🩸💧\n         💧 🩸 💧 💧 💧 🩸💧\n            💧 🩸 💧 💧 🩸 💧\n               💧 🩸💧 🩸 💧\n                   💧  🩸  💧\n                      💧  💧\n                         💧")
            	sleep(0.5)
            	if tim == 5:
            		user.edit_message_text(message.chat.id, message_id=message_id, text="Animation\n      by Shakal")
            		self.start=False
            	user.edit_message_text(message.chat.id,message_id=message_id,text="⁡﻿‌\n\n\n         \n     \n           🩸🩸🩸        🩸🩸🩸\n        🩸 💧💧🩸  🩸💧💧 🩸\n       🩸💧💧💧 🩸 💧💧💧🩸\n        🩸💧 💧 💧 💧 💧 💧🩸\n          🩸💧💧💧💧💧💧 🩸\n            🩸 💧 💧 💧 💧 🩸\n               🩸 💧 💧 💧 🩸\n                  🩸 💧 💧 🩸 \n                     🩸💧 🩸 \n                          🩸  \n                     \n                         ⁡﻿‌")
            	sleep(0.5)
            		
            
        @user.on_message(filters.command('Ukraine'.lower(), prefixes=self.prefix) & filters.me)    
        def ukraine(user, message):
                    self.anima=0
                    self.start=True
                    message_id=message.message_id
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙💙💙         💙💙💙\n💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙\n💛💛💛💙💙💛💛💛💙💙\n💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛\n           💛💛                💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙\n💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛")                
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙\n\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙 💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙      💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙      💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙      💙💙💙💙💙💙💙💙💙💙💙💙💙\n💙💙 💙💙💙💙💙💙💙💙💙💙💙💙\n\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙     💙💙💙💙💙💙💙💙💙💙\n💙      💙     💙💙💙💙💙💙💙💙💙💙💙\n💙      💙     💙💙💙💙💙💙💙💙💙💙💙\n💙      💙     💙💙💙💙💙💙💙💙💙💙💙\n💙💙 💙     💙💙💙💙💙💙💙💙💙💙\n\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙     💙💙💙💙💙💙\n💙      💙     💙 💙     💙💙💙💙💙💙💙\n💙      💙     💙 💙💙💙💙💙💙💙💙💙\n💙      💙     💙 💙     💙💙💙💙💙💙💙\n💙💙 💙     💙 💙     💙💙💙💙💙💙💙\n\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙      💙💙💙💙💙💙\n💙      💙     💙 💙     💙 💙     💙💙💙💙\n💙      💙     💙 💙💙💙 💙💙     💙💙💙\n💙      💙     💙 💙     💙 💙    💙 💙💙💙\n💙💙 💙     💙 💙     💙 💙💙💙💙💙💙\n\n\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙      💙💙💙      💙\n💙      💙     💙 💙     💙 💙     💙 💙     💙\n💙      💙     💙 💙💙💙 💙💙      💙💙💙\n💙      💙     💙 💙     💙 💙    💙  💙     💙\n💙💙 💙     💙 💙     💙 💙💙💙 💙     💙\n\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙      💙💙💙      💙\n💙      💙     💙 💙     💙 💙     💙 💙     💙\n💙      💙     💙 💙💙💙 💙💙      💙💙💙\n💙      💙     💙 💙     💙 💙    💙  💙     💙\n💙💙 💙     💙 💙     💙 💙💙💙 💙     💙\n\n💛     💛💛💛💛💛💛💛💛💛💛💛💛\n💛     💛💛💛💛💛💛💛💛💛💛💛💛\n💛     💛💛💛💛💛💛💛💛💛💛💛💛\n💛     💛💛💛💛💛💛💛💛💛💛💛💛\n💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                    sleep(1)
                    user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙      💙💙💙      💙\n💙      💙     💙 💙     💙 💙     💙 💙     💙\n💙      💙     💙 💙💙💙 💙💙      💙💙💙\n💙      💙     💙 💙     💙 💙    💙  💙     💙\n💙💙 💙     💙 💙     💙 💙💙💙 💙     💙\n\n💛     💛 💛     💛 💛💛💛💛💛💛💛💛\n💛     💛 💛  💛    💛💛💛💛💛💛💛💛\n💛     💛 💛💛      💛💛💛💛💛💛💛💛\n💛     💛 💛   💛   💛💛💛💛💛💛💛💛\n💛💛💛 💛     💛 💛💛💛💛💛💛💛💛")
                    while self.start:
                    	self.anima+=1
                    	print(self.anima)
                    	user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙      💙💙💙      💙\n💙      💙     💙 💙     💙 💙     💙 💙     💙\n💙      💙     💙 💙💙💙 💙💙      💙💙💙\n💙      💙     💙 💙     💙 💙    💙  💙     💙\n💙💙 💙     💙 💙     💙 💙💙💙 💙     💙\n\n💛     💛 💛     💛 💙💙💙💙💙💙💙💙\n💛     💛 💛  💛    💙💙💙💙💙💙💙💙\n💛     💛 💛💛      💙💛💙💛💙💛💙💛\n💛     💛 💛   💛   💛💛💛💛💛💛💛💛\n💛💛💛 💛     💛 💛💛💛💛💛💛💛💛")
                    	sleep(1)
                    	user.edit_message_text(message.chat.id, message_id=message_id, text="💙💙      💙           💙      💙💙💙      💙\n💙      💙     💙 💙     💙 💙     💙 💙     💙\n💙      💙     💙 💙💙💙 💙💙      💙💙💙\n💙      💙     💙 💙     💙 💙    💙  💙     💙\n💙💙 💙     💙 💙     💙 💙💙💙 💙     💙\n\n💛     💛 💛     💛 💙💙💙💙💙💙💙💙\n💛     💛 💛  💛    💙💙💙💙💙💙💙💙\n💛     💛 💛💛      💛💙💛💙💛💙💛💙\n💛     💛 💛   💛   💛💛💛💛💛💛💛💛\n💛💛💛 💛     💛 💛💛💛💛💛💛💛💛")
                    	sleep(1)
                    	if self.anima==3:
                    		user.edit_message_text(message.chat.id, message_id=message_id, text="Glory to Ukraine\n     by Shakal")
                    		self.start=False
                    
        @user.on_message(filters.command('hearth'.lower(), prefixes=self.prefix) & filters.me)
        def serdesko(user, message):
        	self.start= True
        	message_id = message.message_id
        	user.edit_message_text(message.chat.id, message_id=message_id, text="♥️♥️♥️♥️♥️\n                   ♥️\n                   ♥️\n♥️♥️♥️♥️♥️\n                   ♥️\n                   ♥️\n                   ♥️\n♥️♥️♥️♥️♥️")
        	sleep(1)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="🧡🧡🧡🧡🧡\n                   🧡\n                   🧡\n🧡🧡🧡🧡🧡\n🧡\n🧡\n🧡🧡🧡🧡🧡")
        	sleep(1)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁡‌᠎        💚💚\n         💚💚\n         💚💚\n         💚💚\n         💚💚\n         💚💚\n         💚💚")
        	while self.start:
        		sleep(1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text=" ⁢‌⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n\n             ❤️")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n\n                🧡\n           🧡❤️🧡\n                🧡")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                  💛\n             💛🧡💛\n        💛🧡❤️🧡💛\n             💛🧡💛\n                  💛")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                 💚\n            💚💛💚\n       💚💛🧡💛💚\n  💚💛🧡❤️🧡💛💚\n       💚💛🧡💛💚\n            💚💛💚\n                 💚")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                    💙\n               💙💚💙\n          💙💚💛💚💙\n     💙💚💛🧡💛💚💙\n💙💚💛🧡❤️🧡💛💚💙\n     💙💚💛🧡💛💚💙\n          💙💚💛💚💙\n               💙💚💙\n                    💙")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                         💜\n                    💜💙💜\n               💜💙💚💙💜\n          💜💙💚💛💚💙💜\n     💜💙💚💛🧡💛💚💙💜\n💜💙💚💛🧡❤️🧡💛💚💙💜\n     💜💙💚💛🧡💛💚💙💜\n          💜💙💚💛💚💙💜\n               💜💙💚💙💜\n                    💜💙💜\n                         💜")
        		sleep(1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Ми")
        		sleep(0.2)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВ")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ с")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ соз")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ созда")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ создан.")
        		sleep(1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ созда")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ соз")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Ми")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢ ⁢‌⁢")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢Ти")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢Ти чудо")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢ ⁢‌⁢Ти чудова(ий)")
        		sleep(3)
        		user.edit_message_text(message.chat.id, message_id=message_id, text='hearth\n   by Shakal')
        		self.start=False
        	

        @user.on_message(filters.command('spam'.lower(), prefixes=self.prefix) & filters.me)
        def spammer(user, message):
        	stroka=message.text[5:]
        	user.delete_messages(message.chat.id, message.message_id)
        	a=len(stroka)-2
        	num=stroka[a:]
        	slovo= stroka[:a]
        	def spam(num, text):
        		number = 0
        		while True:
        			number+=1
        			user.send_message(message.chat.id, "{}".format(text))
        			if num == number:
        				break
        	spam(num=int(num), text=slovo)

        @user.on_message(filters.command('add'.lower(), prefixes=self.prefix) & filters.me)
        def administartors(user, message):
            if len(message.text) > 4:
                slovo = message.text[4:].replace(' ', '')
                if int(slovo) in self.admins:
                    user.send_message(message.chat.id, 'такой пользователь уже добавлен')
                else:
                    self.admins.append(int(slovo))
                    user.send_message(message.chat.id, f'{slovo} добавлен в список игнорируемых команд')
            else:
                person = message.from_user.id
                self.admins.append(person)
                user.send_message(message.chat.id, 'Пользователь добавлен в список игнорируемых команд')

        @user.on_message(filters.command('del'.lower(), prefixes=self.prefix) & filters.me)
        def administartor(user, message):
            if len(message.text) > 4:
                slovo = message.text[4:].replace(' ', '')
                if int(slovo) in self.admins:
                    self.admins.remove(int(slovo))
                    user.send_message(message.chat.id, f'{slovo} удален из списка игнорируемых команд')
                else:
                    user.send_message(message.chat.id, "Такого пользователя нет в списке сначала нужно добавить")
            else:
                person = message.from_user.id
                self.admins.remove(person)
                user.send_message(message.chat.id, 'Пользователь удален из списка игнорируемых команд')

        @user.on_message(filters.command('id'.lower(), prefixes='my_') & filters.private)
        def id_users(user, message):
            key = message.from_user.first_name
            value = int(message.from_user.id)
          #  if {key:value} in self.key:
     #           user.send_message(message.chat.id,"gttt")
    #        else:
            self.key[key] = value
            user.send_message(message.chat.id, "{} you ID is `{}`".format(message.from_user.first_name, message.from_user.id))

        @user.on_message(filters.command('info'.lower(), prefixes=self.prefix) & filters.me)
        def otvet_mne(user, message):
            user.send_message(message.chat.id, "Владелец кода Shakal\n `^-^info`\n `+add`\n`-delete`\n `my_id` for all\n`+members`\n`+spam` text количество максимум 99")
            user.send_message(message.chat.id, text= "Animations: \n `+hearth` \n `+hearths`\n `+Ukraine` \n `+void`\n `+surprise`")


        @user.on_message(filters.text & filters.private)
        def otvet_private(user, message):
            if message.text == 'stop':
            	self.start = False
            if message.from_user.id == 1404274376:
            	print(self.a)
            	self.a+=1
            #	if self.a==11:
            #		self.a=0
            #		user.send_message(1404274376, "Стыцько!!!")
            if "вадим" in message.text.lower():
            	user.send_message(message.chat.id, "Чего? *****это автоответчик***")
            if message.text == 'xxx':
            	self.start=True
            	while self.start:
            		user.send_message(message.chat.id, "Russian warship Fuck You!")
            if message .text == "stop":
            	self.start=False
            if message.from_user.id in self.admins: pass
            elif message.text.lower() in self.privetstvie:
                hey = random.choice(self.otvet)
                user.send_message(message.chat.id, "{}  {} ".format(hey, message.from_user.first_name))
            else:pass

        @user.on_message(filters.text & filters.group)
        def otvet_group(user, message):
            if message.from_user.id in self.admins: pass
            elif message.text.lower() in self.privetstvie:
                hey = random.choice(self.otvet)
                user.send_message(message.chat.id, "{}  {}".format(hey, message.from_user.first_name))
            else:pass

        user.run()

if __name__ == "__main__":
    Automess()