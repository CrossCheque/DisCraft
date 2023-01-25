#discraft.py
import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

#start working on a steaming log of py
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#let's get some authentication
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#set a channel command prefix
bot = commands.Bot(command_prefix="!")

## COMMANDS ##
class BleepBloop(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(brief='Helpful Text', description='One Ping to rule them all, One Pong to find them, One Ding to dong them all, and in the darkness... ping them.')
	async def ping(self, ctx):
		await ctx.send('Pong!')

	@commands.command(brief='Less Helpful Text', description="Sometimes you just don't know what you're doing.")
	async def pong(self, ctx):
		await ctx.send("Hold on, that's my line!")

	@commands.command(hidden=True)
	async def bitch(self, ctx):
		await ctx.send('ur mom a hoe',mention_author=True)

class ServerCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(brief='Start!',description='Open a new shell, start a vanilla server.')
	async def start(self, ctx):
		await ctx.send("Starting!")
		os.system("screen -dmS vanillaMC bash -c 'cd servers/vanilla; ./vanillastart.sh'")
		
	@commands.command(brief='Stop!',description='Stop the vanilla shell, hopefully gracefully.')
	async def stop(self, ctx):
		await ctx.send("Haulted!")
		os.system("screen -p 0 -S vanillaMC -X eval 'stuff "stop"\015'")
		
bot.add_cog(BleepBloop(bot))
bot.add_cog(ServerCommands(bot))
bot.run(TOKEN)
