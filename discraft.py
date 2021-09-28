#discraft.py
import os
import discord
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')
        
client.run(TOKEN)

