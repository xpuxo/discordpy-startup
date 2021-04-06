import discord

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_reaction_add(reaction, user):
    # author: リアクションがついたメッセージを書いた人
    author = reaction.message.author
    await client.send_message(author, f"{user} さんがリアクションをしました")



bot.run(token)
