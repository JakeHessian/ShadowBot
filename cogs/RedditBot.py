import discord
from discord.ext import commands
import asyncio
import aiohttp
import random


class RedditBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        loop = asyncio.get_event_loop()
        self.client = aiohttp.ClientSession(loop=loop)
        self.exts = ['.jpg', '.png', '.gif', '.bmp']
        self.urlPrefix = "https://reddit.com/r/"

    @commands.Cog.listener()
    async def on_ready(self):
        print("Reddit grabber loaded.")

    @ commands.command(pass_context=True)
    async def get(self, ctx, arg):
        for x in range(20):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://www.reddit.com/r/"+arg+"/hot.json?limit=50") as response:
                    # async with session.get(f"https://www.reddit.com/r/"+arg+"/random.json") as response:
                    j = await response.json()
            try:
                r = random.randint(0, len(j["data"]["children"]))
                data = j["data"]["children"][r]["data"]
            except:
                await ctx.send("Error getting that.")
                return
            image_url = data["url"]
            #print(image_url, image_url[-4])
            if image_url[-4:] in self.exts:
                break
            image_url = "no image found"
        #print("Image url:", image_url)
        title = data["title"]
        em = discord.Embed(
            description=f"[**{title}**]({image_url})", colour=discord.Colour.blue())
        em.set_image(url=image_url)
        em.set_footer(icon_url=ctx.author.avatar_url,
                      text=f"Requested by {ctx.author}")
        await ctx.send(embed=em)

    async def get_json(seklf, client, url):
        async with client.get(url) as response:
            assert response.status == 200
            return await response.read()


def setup(bot):
    bot.add_cog(RedditBot(bot))
