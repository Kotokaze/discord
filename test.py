import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as ${self.user}!')

  async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))

def main():
	load_dotenv()
	DISCORD_TOKEN = getenv('DISCORD_TOKEN')
	client = MyClient()
	client.run(DISCORD_TOKEN)

if __name__ == '__main__':
		main()
