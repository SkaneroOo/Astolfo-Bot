import discord
from discord.ext import commands
import random
import praw
import giphy_client
from giphy_client.rest import ApiException

reddit = praw.Reddit(client_id=os.environ.get('REDDIT_ID'), client_secret=os.environ.get('REDDIT_SECRET'), user_agent='testscript by /u/SkaneroOo')
giphy_token = os.environ.get('GIPHY_TOKEN')
api_instance = giphy_client.DefaultApi()

class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help='Send random Astolfo picture from r/Astolfo', brief='Send random Astolfo picture', usage=';astolfo')
	@commands.guild_only()
	async def astolfo(self, ctx):
		submissions = reddit.subreddit('Astolfo').hot()
		post_to_pick = random.randint(1, 10)
		for i in range(0, post_to_pick):
			submission = next(x for x in submissions if not x.stickied)
		embed = discord.Embed(color=0xee62d3)
		embed.set_image(url=submission.url)
		await ctx.send(embed=embed)

	'''@commands.command(brief='Insult someone (wip)', help='Send insult gif directed to mentioned user', usage=';insult  @╲⎝⧹SkaneroOo⧸⎠╱#6169')
	@commands.guild_only()
	async def insult(self, ctx, *args):
		try:
			if args[0] and ctx.message.mentions[0]:
				response = api_instance.gifs_search_get(giphy_token, 'anime insult', limit=10, rating='g')
				lst = list(response.data)
				gif = random.choices(lst)
				await ctx.send('@' + str(ctx.message.mentions[0]) + ' got insulted.\n' + str(gif[random.randint(0,len(gif)-1)].url))
		except IndexError:
			await ctx.send('I don\'t know who you want to insult')'''

	@commands.command(aliases=['m'], help='Send random meme from subreddit r/memes', brief='Send random meme', usage=';meme')
	@commands.guild_only()
	async def meme(self, ctx):
		submissions = reddit.subreddit('memes').new()
		post_to_pick = random.randint(1, 10)
		for i in range(0, post_to_pick):
			submission = next(x for x in submissions if not x.stickied)
		embed = discord.Embed(color=0xee62d3)
		embed.set_image(url=submission.url)
		await ctx.send(embed=embed)

	@commands.command(aliases=['am'], help='Send random anime meme from r/Animemes', brief='Send random anime meme', usage=';animeme')
	@commands.guild_only()
	async def animeme(self, ctx):
		submissions = reddit.subreddit('Animemes').new()
		post_to_pick = random.randint(1, 10)
		for i in range(0, post_to_pick):
			submission = next(x for x in submissions if not x.stickied)
		embed = discord.Embed(color=0xee62d3)
		embed.set_image(url=submission.url)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(fun(bot))