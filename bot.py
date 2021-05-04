# bot.py
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


bot = commands.Bot(command_prefix='/')
bot.load_extension("handlers.commands")
bot.run(TOKEN)
