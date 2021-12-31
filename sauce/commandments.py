#commandments.py

from discord.ext import commands

class BleepBloop(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(brief='Syemour!', description='I must feed.')
	async def testme(self, ctx):
		await ctx.send('FEED ME SEYMOUR!')

def setup(bot):
	bot.add_command(testme)