import discord
from discord.ext import commands
from handlers.modules.apex_module import ApexModule


# Commands that are available at this moment
class AllCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def apex(self, ctx):
        await ApexModule.on_message(ctx.message)


def setup(bot):
    bot.add_cog(AllCommands(bot))
