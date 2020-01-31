import asyncio
from discord.ext import commands, tasks
import discord
#import praw
from random import randint
import os

TOKEN = os.environ.get('DISCORD_TOKEN')
BOT_PREFIX=(';')
bot = commands.Bot(command_prefix = BOT_PREFIX)
# mywaifulist.moe/random
#reddit = praw.Reddit(client_id='https://www.reddit.com', client_secret='Va3_xSGvN8qkbzKlu9s9FdmfJck', user_agent='testscript')

bot.remove_command('help')
OWNERS = ['215553356452724747']
initial_extensions = ['Cogs.fun', 'Cogs.utilities', 'Cogs.nsfw']
blacklists = {
	'servers':[], 
	'users':[], 
	'channels':[]
}


if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

@bot.command(pass_context=True, help='OWNER ONLY', brief='OWNER ONLY', usage='OWNER ONLY')
async def reload(ctx):
	if str(ctx.message.author.id) in OWNERS:
		text = ''
		for extension in initial_extensions:
			try:
				bot.reload_extension(extension)
				text += 'Succesfully reloaded ' + str(extension) + ' :white_check_mark:\n'
				print('Reloaded ' + str(extension))
			except:
				print('Failed to reload ' + str(extension))
				text += 'Failed to reload ' + str(extension) + ' :negative_squared_cross_mark:\n'
		await ctx.send(text)

@bot.event
async def on_message(message):
	if message.channel.name == 'todo' and len(message.channel_mentions) > 0:
		if message.channel_mentions[0].name == 'todo':
			await message.pin()
			await message.channel.purge(limit=1)
	elif not (message.author.id in blacklists['users'] or message.channel.id in blacklists['channels'] or message.guild.id in blacklists['servers']):
		await bot.process_commands(message)

@bot.event
async def on_ready():
	print('------------')
	print('Logged in as:')
	print(bot.user.name)
	print(bot.user.id)
	print('Connected to ' + str(len(bot.guilds)) + ' servers.')
	print('------------')

bot.run(TOKEN)