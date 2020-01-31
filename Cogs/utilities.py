import discord
from discord.ext import commands
import random


class utils(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(brief='Grabs user/bot avatar', help='Sends mentioned user/bot avatar', usage=';avatar @╲⎝⧹SkaneroOo⧸⎠╱#6169')
	@commands.guild_only()
	async def avatar(self, ctx, *args):
		try:
			if args[0] and ctx.message.mentions[0]:
				url = ctx.message.mentions[0].avatar_url
				embed = discord.Embed(title='Here you are.', color=0xee62d3)
				embed.set_image(url=url)
				await ctx.send(embed=embed)
		except IndexError:
			await ctx.send('I don\'t know whose avatar you want to grab.')


	@commands.command(brief='Send this message', help='Send this message', usage=';help')
	@commands.guild_only()
	async def help(self, ctx, *args):
		if len(args) == 0:
			embed = discord.Embed(title='My commands:', color=0xee62d3)
			num = 0
			for a, b in self.bot.cogs.items():
				com = ''
				for c in b.get_commands():
					com += c.name + ' - ' + c.brief + '\n'
					num += 1
				embed.add_field(name='**' + a.upper() + '**', value=com, inline=False)
			embed.set_footer(text="Currently " + str(num) + ' commands.')
			await ctx.send(embed=embed)
		else:
			coms = []
			for com in self.bot.commands:
				coms.append(com.name)
			if args[0] in coms:
				embed = discord.Embed(title='**' + args[0] + '**', color=0xee62d3)
				for com in self.bot.commands:
					if com.name == args[0]:
						command = com
				embed.add_field(name='**help: **', value=command.help, inline=False)
				embed.add_field(name='**Usage: **', value=command.usage, inline=False)
				if len(command.aliases) != 0:
					embed.add_field(name='**Aliases: **', value=str(command.aliases).strip("[]'").replace("', '", ', '), inline=False)
				await ctx.send(embed=embed)
			else:
				await ctx.send('I don\'t know such command. Check **;help** for available commands.')



def setup(bot):
	bot.add_cog(utils(bot))