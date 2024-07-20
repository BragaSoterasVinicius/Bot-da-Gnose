import os
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from botdagnose import gnose_maker

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
    
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Que porra é sessa caraio')
    try: 
        response: str = gnose_maker(user_message)
        print(response)
        if response != None:
            await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} tá correndo!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    
    username: str = str(message.author)
    user_messsage: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_messsage}"')
    await send_message(message, user_messsage)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()