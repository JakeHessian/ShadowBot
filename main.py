import discord
from discord.ext import commands
import asyncio
from random import randint
from Interview import *
from prawcore.exceptions import NotFound

questions = []

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)


@ bot.command()
async def ping(ctx):
    await ctx.send("Shadow pong!")


@ bot.command()
@ commands.has_permissions(administrator=True)
async def clear(ctx):
    channel = discord.utils.get(ctx.guild.channels, name="📝-application-🤘")
    await channel.purge()
    await channel.send("To start an application, type **.apply**")
    # await channel.send("""Please copy/paste and post application:

    # Enter your Steam profile link
    # Why do you want to join the clan and what can you contribute?
    # What are your best Rust skills (PvPing, Farming, Monuments, Oil Rig, Bradley)
    # How many hours do you have in Rust?
    # Do you agree to use the Recruit base untill promoted/trusted?""")


@ bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game("with Python"))
    print("Bot ready!")
    #bot.add_cog(Applications(questions, bot))
    #print("Applications ready")


@ bot.event
async def on_member_join(member):
    print("new user joined... sending them welcome DM")
    await member.send("Hello {}!:smiley: To join **The Shadows** please type **.apply** in the **applications** channel. Thanks!".format(member.name))


@ bot.event
async def on_member_leave(member):
    print("User was removed {}".format(member.name))


inFile = open("token.txt", 'r')
token = inFile.read()
inFile.close()
bot.load_extension("cogs.Applications")
bot.load_extension("cogs.RedditBot")
bot.run(token)
