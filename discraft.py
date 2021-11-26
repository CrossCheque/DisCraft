#discraft.py
import os
import discord
import dotenv #import environment file control for TOKEN
import subprocess #import python utility for shell execution
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

## COMMANDS ##
@bot.command(
	help="Start a server.",
	brief="Starts the server."
)
async def start(ctx):
#	subprocess.call(['sh', '/servers/vanilla/vanillaserver.sh'])
	os.system('screen -dmS vanillaserver')
	os.system('screen -rS vanillaserver')
	os.system('cd "./servers/vanilla"')
	os.system('./vanillaserver.sh')
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