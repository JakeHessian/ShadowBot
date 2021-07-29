import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import random

class WipeReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.creatingFlag = False
        self.questions = ["Enter the server name:","Enter the server IP:","Enter the wipe time (%m/%d/%y %H:%M:%S):"]
        self.author = ''
        self.questionCounter = 0
        self.answers = []
        self.channel = ''
        self.gamers = ['pima','clover','marc']

    @ commands.command()
    @ commands.has_permissions(administrator=True)
    async def wipeStart(self, ctx):
        game = discord.Game("Creating new Wipe Reminder")
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        self.author = ctx.message.author
        self.creatingFlag = True

    @commands.Cog.listener()
    async def on_message(self, message):
        print("Is user bot?")
        if (message.author.bot == False):
            print("No")
            if (self.creatingFlag):
                if (message.author == self.author):
                    if(self.author != '' or self.author != None):
                        await self.author.send(self.questions[self.questionCounter])
                        self.questionCounter += 1
                        self.answers.append(message.content)
                        #print(self.answers)
                        if (self.questionCounter == len(self.questions)):
                            self.creatingFlag = False
                            self.questionCounter = 0
                            game = discord.Game("with Clover's balls")
                            await self.bot.change_presence(status=discord.Status.idle, activity=game)
                            await self.printWipe("server name goes here")
        else:
            print("yes")

    async def printWipe(self, serverName):
        embed=discord.Embed(title=serverName, description="07/24/21 08:00")
        gamers = ''
        for name in self.gamers:
            gamers = gamers + "\n" + name
        embed.set_author(name="--Wipe--")
        embed.set_image(url="https://files.rustmaps.com/img/214/412e38ba-b07f-4ae2-b234-c3f0cb30f828/FullMap.png")
        embed.set_thumbnail(url="https://i.imgur.com/0TjUOAT.png")
        embed.add_field(name = "Gamers", value=gamers, inline=False)
        embed.set_footer(text="Coded by Clover")
        await self.author.send(embed=embed)
    @commands.Cog.listener()
    async def on_ready(self):
        print("WipeReminder loaded.")


def setup(bot):
    bot.add_cog(WipeReminder(bot))
