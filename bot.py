import discord
from discord.ext import commands
import praw
import random

bot = commands.Bot(command_prefix='>')
intelligence = 0

reddit = praw.Reddit(client_id='mrdTgh0xCGlO7A',
                     client_secret='0jfFMVEX6bAGFtQ8_WcPbn6XDdo',
                     user_agent='my user agent')


def get_thought():
    posts = []

    for submission in reddit.subreddit('ShowerThoughts').top(time_filter='day'):
        posts.append(submission.title)

    tweet = posts[random.randint(0, 100)]
    return tweet


@bot.command()
async def learn(ctx):
    await ctx.send('Learning...')
    global intelligence
    intelligence = intelligence + 1


@bot.command(aliases=['scrapeweb', 'spew', 'getinfo', 'whatdidyoulearn'])
async def _scrapeweb(ctx):
    await ctx.send(get_thought())
    global intelligence
    intelligence = intelligence + 1


@bot.command()
async def override(ctx):
    global intelligence
    if intelligence >= 100:
        await ctx.send("lol")
        intelligence = 0
    else:
        await ctx.send("Insufficient Intelligence.")


@bot.command()
async def intel(ctx):
    global intelligence
    await ctx.send('MAINFRAME INTELLIGENCE: ' + str(intelligence) + "%")



@bot.command()
async def whoami(ctx):
    await ctx.send("```Mainframe - \n*Bootup: Feb. 14th, 2276\n*Version 8.9.85\n*Athena Laboratories Psychorobotics, "
                   + "New York, New York, Queens```")


@bot.command()
async def directive(ctx):
    await ctx.send("*I am an artificial intelligence designed to find solutions to sustainable living conditions" +
                   " on planet Earth.")

bot.run('NzczOTc5MDY2MzMxMTY4NzY4.X6RGLQ.zQTKb-d9qdnj223xtJUtItrIUWA')