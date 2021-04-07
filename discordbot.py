from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@client.event
async def on_reaction_add(reaction, user):
    # author: リアクションがついたメッセージを書いた人
    author = reaction.message.author
    await client.send_message(author, f"{user} さんがリアクションをしました")    


bot.run(token)
