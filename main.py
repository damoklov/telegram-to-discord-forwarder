import time
import discord
import json
from telethon import TelegramClient, events
from telethon import errors


def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


config = read_config('config.json')

TG_HASH = config["TG_HASH"]
TG_API = config["TG_API"]
DC_TOKEN = config["DC_TOKEN"]
SERVER_ID = config["SERVER_ID"]
CHANNEL_ID = config["CHANNEL_ID"]
CHATS = [config["CHATS"]]

client = TelegramClient("Test", TG_API, TG_HASH)


async def send_message(message):
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = False
    intents.presences = False
    discord_client = discord.Client(intents=intents)

    @discord_client.event
    async def on_ready():
        print(f'{discord_client.user} is sending a new message')
        server = discord_client.get_guild(SERVER_ID)
        channel = server.get_channel(CHANNEL_ID)
        await channel.send(message)
        await discord_client.close()

    await discord_client.start(DC_TOKEN)
    print("Done")


@client.on(events.NewMessage(chats=CHATS))
async def handle_new_message(event):
    print("New message!")
    if event.message.web_preview:
        print("Web Preview")
    elif event.message.photo:
        print("Photo")
    elif event.message.document:
        print("Document")
    elif event.message.text:
        print("Text message")
        original_message = event.message.message.split('\n')[1:-2]
        original_message[0] = ":e_mail: " + original_message[0]
        original_message[1] = ":envelope_with_arrow: " + original_message[1]
        original_message[2] = ":moneybag: " + original_message[2]
        original_message[3] = ":ringed_planet: " + original_message[3]
        original_message[4] = ":timer: " + original_message[4] + '\n---------------------------\n'
        message_text = '\n'.join(original_message)
        await send_message(message_text)


if __name__ == '__main__':
    client.start()

    try:
        client.run_until_disconnected()
    except errors.FloodWaitError as e:
        print('Waiting for ', e.seconds)
        time.sleep(e.seconds)
