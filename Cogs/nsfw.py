import discord
from discord.ext import commands
import random

answer = ['Check this you pervert!',
'Do it fast boy! Nobody watching!',
'That especially for you :heart:',
'Here you go!',
'Ugh... Ewl',
'Do you want more?',
'Thats my boy!',
'Just remember to remove it when you done :stuck_out_tongue_winking_eye:',
'Done! But you know what? I think you should go and find a real girlfriend.']

class nsfw(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['doujin', 'djs'],brief='Send random doujinshi link', help='Send random doujinshi link from nhentai.net (NSFW channel only)', usage=';doujinshi')
	@commands.guild_only()
	async def doujinshi(self, ctx):
		if ctx.message.channel.is_nsfw():
			await ctx.send(answer[random.randint(0,8)])
			await ctx.send('https://nhentai.net/g/' + str(random.randint(1,300000)) + '/')
		else:
			await ctx.send('I can\'t send it here')






def setup(bot):
	bot.add_cog(nsfw(bot))