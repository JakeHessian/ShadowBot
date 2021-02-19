import discord
from discord.ext import commands
import asyncio
from Interview import *


class Applications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.interviews = []
        self.QUESTIONS = []
        self.appChannelID = 0
        self.shadowRecruitRole = None
        self.farmerRole = None
        print("Applications Cog: loading apllication questions...")
        questionFile = open("AppQuestions.txt", 'r')
        for item in questionFile:
            self.QUESTIONS.append(item)
        questionFile.close()
        print("done")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Reactions loaded.")

    @ commands.command(pass_context=True)
    async def apply(self, ctx):
        global appChannelID
        # pre load the channel
        temp = discord.utils.get(
            ctx.guild.text_channels, name='applications')
        # pre load roles from this context
        self.appChannelID = int(temp.id)
        self.shadowRecruitRole = discord.utils.get(
            ctx.message.author.guild.roles, name="Shadow Recruits")
        self.farmerRole = discord.utils.get(
            ctx.message.author.guild.roles, name="FARMER")
        await ctx.send("Starting application. Please check your DMs **{}** 👍".format(ctx.message.author.name))
        await ctx.author.send("  --  Hello **{}**! Beginning your application:  --  \n  --  To cancel application, send **.cancel**".format(ctx.message.author.name))
        print("Creating new interview instance")
        self.interviews.append(Interview(self.QUESTIONS, ctx.author))
        await ctx.author.send(self.interviews[-1].getNextQuestion())

    @commands.Cog.listener()
    async def on_message(self, message):
        #print("Message here")
        # may be easier on resources to checkout if interviews exist (N)
        if (len(self.interviews) != 0 and message != ".cancel"):
            # check if message is a private channel
            if (message.channel.type == discord.ChannelType.private):
                #print("Received private message")
                # check if the message is from a bot
                if (message.author != self.bot.user):
                    # check to see if message author has an interview open
                    for x in range(len(self.interviews)):
                        if (self.interviews[x].getMember() == message.author):
                            member = self.interviews[x].memberObject
                            # user has open interview
                            # record the response for question
                            self.interviews[x].responses.append(
                                message.content)
                            # print(interviews[x].responses)
                            # send next question
                            if (self.interviews[x].isEmpty() == False):
                                await message.author.send(self.interviews[x].getNextQuestion())
                            else:
                                # user is done interview
                                await message.author.send("""
                                :shamrock: Application complete, sending to Admins.:shamrock:
                                If they're any issues with the bot, please contact Cloverleaf.""")
                                # create embed
                                embed = discord.Embed(
                                    title="User {}'s Application ID:{}".format(
                                        message.author.name, message.author.id),
                                    colour=discord.Colour.green(),
                                    description="""Click 👩‍🌾 to accept as **Farmer**
                                    Click 🔫 to request **PvP tryout**
                                    Click to ⛔ to **deny.**"""
                                )
                                # print(interviews[x].responses)
                                #print("Length of questions:", len(questions))
                                for y in range(len(self.QUESTIONS)):
                                    embed.add_field(
                                        name=self.QUESTIONS[y], value=self.interviews[x].responses[y], inline=False)
                                embed.set_footer(
                                    text="Bot coded by Cloverleaf")
                                # print(appChannelID)
                                channel = self.bot.get_channel(
                                    self.appChannelID)
                                await channel.send(embed=embed)
                                self.interviews.pop(x)
                                await asyncio.sleep(0.5)
                                lastMessage = channel.last_message
                                await lastMessage.add_reaction("👩‍🌾")
                                await lastMessage.add_reaction("🔫")
                                await lastMessage.add_reaction("⛔")
                            break  # no need to look through other interviews
        # await self.bot.process_commands(message)
# ID:376521130791665675
     # 376521130791665675 376521130791665675

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if (user != self.bot.user and reaction.message.author == self.bot.user):
            if (len(reaction.message.embeds) != 0):
                if(user.top_role.permissions.administrator):
                    print("reaction detected")
                    embed = reaction.message.embeds[0].to_dict()
                    id = int(embed.get("title")[-18:])
                    # print(id)
                    member = reaction.message.guild.get_member(id)
                    channel = self.bot.get_channel(
                        self.appChannelID)
                    if (member == None):
                        #print("User not found.")
                        return
                    if(str(reaction.emoji) == "👩‍🌾"):
                        # print("Adding role to user.")
                        # await member.add_roles(self.farmerRole)
                        await member.add_roles(self.shadowRecruitRole)
                        # await discord.Member.add_roles(member, self.farmerRole)
                        # await discord.Member.add_roles(member, self.shadowRecruitRole)
                        # print("Complete")
                        await channel.send("User: **{}** was accepted. as **{}**".format(member.name, self.farmerRole.name))
                        await member.send("Congratulations, **{}** you have been accepted as **{}** 👩‍🌾".format(member.name, self.farmerRole.name))
                    elif(str(reaction.emoji) == "🔫"):
                        await member.add_roles(self.shadowRecruitRole)
                        # await discord.Member.add_roles(member, self.shadowRecruitRole)
                        # print("Complete")
                        await channel.send("User: **{}** was accepted. as **{}** + PvP role, pending tryout.".format(member.name, self.shadowRecruitRole.name))
                        await member.send(
                            """
                        Congratulations, **{}** you have been accepted as **{}**. 🔫
                        Note: You must tryout with **Marc** to earn the PvP Role.""".format(member.name, self.farmerRole.name))
                    elif(str(reaction.emoji) == "⛔"):
                        await channel.send("User was declined. Closing application.")
                        await member.send("Sorry, you have been denied. Goodluck on your search.")

    @ commands.command()
    async def cancel(self, ctx):
        if (len(self.interviews) != 0):
            if (ctx.message.channel.type == discord.ChannelType.private):
                for x in range(len(self.interviews)):
                    if (self.interviews[x].getMember() == ctx.message.author):
                        self.interviews.pop(x)
                        print("Canceling application with", ctx.author.name)
                        await ctx.send("Canceling your application. To reapply, type **APPLY**")


def setup(bot):
    bot.add_cog(Applications(bot))
