from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
import discord

client = discord.Client()

@client.event
async def on_reaction_add(reaction, user):
    
    author = reaction.message.author
    await client.send_message(author, f"{user} さんがリアクションをしました")


bot.run(token)
