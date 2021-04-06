from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
import discord
from discord_reactor.config.token import token


class Reactor(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        author = reaction.message.author
        await author.send(f"{user} さんがリアクションをしました")
        print(f"sent message to {author}")


bot.run(token)
