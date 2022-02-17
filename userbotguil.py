from pyrogram import Client, filters
import random

class Automess():
    def __init__(self):
        self.api_id = 9958356
        self.api_hash = "8895b2a2b674f00658660440ef8adcbb"
        self.admins = [697798016]
        self.key = {"Shakal":697798016}
        # Конфиг
        self.privetstvie = ['hi','hello','hey','пр',"привет","доров","здрасте","приветик","ку"]
        self.otvet = ["Hi","Приветик","Ку","Привет"]
        self.prefix = ["+", "-", "^-^"]

        self.word = filters.text

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
            if {key:value} in self.key:
                user.send_message(message.chat.id,"gttt")
            else:
                self.key[key] = value
                user.send_message(message.chat.id, "{} you ID is `{}`".format(message.from_user.first_name, message.from_user.id))

        @user.on_message(filters.command('info'.lower(), prefixes=self.prefix) & filters.me)
        def otvet_mne(user, message):
            user.send_message(message.chat.id, "Владелец кода Shakal\n ^-^info\n +add\n-delete\n my_id for all")


        @user.on_message(filters.text & filters.private)
        def otvet_private(user, message):
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