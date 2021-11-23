#discraft.py
import os
import discord
import subprocess #import python utility for shell execution
from discord.ext import commands
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')
        

#Open server shell
#os.system(screen -p minecraft -X vanillaServer) 
#need to test window names, vanillaServer should be same as .sh

## COMMANDS ##
@bot.command(
	help="Inovkes the server start shell.",
	brief="Starts the server."
)
async def start(ctx):
	subprocess.call(['sh', './Users/harbinger/Downloads/Minecraft/vanillaserver.sh'])
#bot calls OS to start new shell

@bot.command(
	help="Terminates active Minecraft server, hopefully gracefully.",
	brief="Stops the server."
)
async def start(ctx):
	os.system(screen -p minecraft -X vanillaServer "stop\015")
#bot forwards STOP command to minecraft shell

bot.run(DISCORD_TOKEN)