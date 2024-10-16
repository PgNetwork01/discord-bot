from discord.ext import commands
import discord
from config import TOKEN
import logging
from general import GeneralCommands
from moderation import ModerationCommands
from economy import EconomyCommands

# Enable logging
# logging.basicConfig(level=logging.DEBUG)

intents = discord.Intents.default()
intents.members = True  # Enable the members intent if you need to access member-related events
intents.message_content = True  # Enable the members intent if you need to access member-related events
intents.messages = True  # Enable the messages intent to receive messages

# Define the bot prefix
bot = commands.Bot(command_prefix='.', intents=intents)

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))
    print("Connected to General system!")
    await bot.add_cog(ModerationCommands(bot))
    print("Connected to Moderation systems!")
    await bot.add_cog(EconomyCommands(bot))
    print("Connected to Economy system!")
    
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
    await setup(bot)

bot.run(TOKEN)
