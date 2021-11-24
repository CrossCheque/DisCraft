#discraft.py
import os
import discord
import dotenv #import environment file control for TOKEN
import subprocess #import python utility for shell execution
from discord.ext import commands
from dotenv import load_dotenv

#client = discord.Client()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

#@client.event
#async def on_ready():
#        print(f'{client.user} has connected to Discord!')
#THIS BIT NO WORKIE :<

## COMMANDS ##
@bot.command(
	help="Inovkes the server start shell.",
	brief="Starts the server."
)
async def start(ctx):
	subprocess.call(['sh', '/Users/harbinger/Downloads/Minecraft/vanillaserver.sh'])
#bot calls OS to start new shell
#change this to a screen command, will fix issue with muliplexing the discraft directory and shell. -AV

@bot.command(
	help="Terminates active Minecraft server, hopefully gracefully.",
	brief="Stops the server."
)
async def stop(ctx):
	os.system("screen -S minecraft -p 0 -X vanillaserver 'stop\015'")
#bot forwards STOP command to minecraft shell

bot.run(TOKEN)