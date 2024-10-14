# bot.py
from discord.ext import commands
import discord
import random
import datetime
import asyncio
import os

# Load the bot token from config
from config import TOKEN

import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Rest of your bot code...


intents = discord.Intents.default()
intents.members = True  # Enable the members intent if you need to access member-related events
intents.message_content = True  # Enable the members intent if you need to access member-related events
intents.messages = True  # Enable the messages intent to receive messages

# Define the bot prefix
bot = commands.Bot(command_prefix='.', intents=intents)

#Load cogs asynchronously
async def load_cogs():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded {filename[:-3]} cog successfully.')
            except Exception as e:
                print(f'Failed to load {filename[:-3]} cog: {e}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, that command does not exist. | [*Debug Session*]")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing a required argument. Please check the command usage. | [*Debug Session*]")
    else:
        await ctx.send(f"An error occurred: {error} | [*Debug Session*]")
        logging.error(f"Error in command '{ctx.command}': {error} | [*Debug Session*]")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

bot.run(TOKEN)
