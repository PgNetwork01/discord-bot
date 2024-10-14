# commands/general.py
from discord.ext import commands
import discord
import random
import datetime
import asyncio

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', description="Lists all available commands.")
    async def help(self, ctx):
        help_text = (
            "**General Commands:**\n"
            "`help` - Lists all available commands.\n"
            "`info` - Information about the bot.\n"
            "`ping` - Checks bot latency.\n"
            "`stats` - Displays bot statistics.\n"
            "`uptime` - Displays how long the bot has been online.\n"
            "`serverinfo` - Displays information about the server.\n"
            "`userinfo [member]` - Displays information about a user.\n"
            "`roles` - Lists all server roles.\n"
            "`invite` - Generates an invite link for the server.\n"
            "`feedback [message]` - Sends feedback.\n"
            "`emoji` - Shows a set of emojis.\n"
            "`rules` - Displays server rules.\n"
            "`say [message]` - Repeats the message.\n"
            "`choose [option1, option2, ...]` - Randomly chooses an option.\n"
            "`fortune` - Gives a random fortune.\n"
            "`echo [message]` - Echoes back the message.\n"
            "`howdy` - Sends a friendly greeting.\n"
            "`greeting` - Sends a general greeting.\n"
            "`welcome` - Welcomes new members.\n"
            "`goodbye` - Says goodbye to members.\n"
            "`support` - Provides support information.\n"
            "`version` - Displays bot version.\n"
            "`contact` - Information on how to contact the bot team.\n"
            "`botinfo` - Information about the bot.\n"
            "`serverstats` - Displays server statistics.\n"
            "`membercount` - Displays the number of members in the server.\n"
            "`channelinfo` - Shows information about the current channel.\n"
            "`whois [member]` - Shows user ID and info.\n"
            "`avatar [member]` - Shows user's avatar.\n"
            "`pingrole [role]` - Pings a specific role.\n"
            "`reminder [time] [message]` - Sets a reminder.\n"
            "`translate [language] [text]` - Translates text to a given language.\n"
            "`servericon` - Displays server icon.\n"
            "`suggest [suggestion]` - Sends a suggestion.\n"
            "`bugreport [report]` - Sends a bug report.\n"
            "`tips` - Provides tips for users.\n"
            "`countdown [seconds]` - Starts a countdown.\n"
            "`dailyfact` - Provides a random daily fact.\n"
            "`fact` - Provides a random fact.\n"
            "`announce [message]` - Sends an announcement.\n"
            "`messagecount` - Counts messages in the current channel.\n"
            "`check` - Checks the bot's status.\n"
            "`currenttime` - Displays the current time.\n"
            "`timezone` - Displays the bot's timezone.\n"
            "`alert [message]` - Sends an alert message.\n"
            "`announcements` - Shows where to find announcements."
        )
        await ctx.send(help_text)

    @commands.command(name='info', description="Information about the bot.")
    async def info(self, ctx):
        await ctx.send("I am a helpful bot created to assist you!")

    @commands.command(name='ping', description="Checks bot latency.")
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(name='stats', description="Displays bot statistics.")
    async def stats(self, ctx):
        # Replace with actual stats if available
        await ctx.send("Bot stats: Online and running smoothly!")

    @commands.command(name='uptime', description="Displays how long the bot has been online.")
    async def uptime(self, ctx):
        # Replace with actual uptime calculation
        await ctx.send("Bot uptime: 1 hour, 30 minutes.")

    @commands.command(name='serverinfo', description="Displays information about the server.")
    async def serverinfo(self, ctx):
        server = ctx.guild
        embed = discord.Embed(title=f"{server.name} Info", color=0x00ff00)
        embed.add_field(name="Owner", value=server.owner)
        embed.add_field(name="Member Count", value=server.member_count)
        embed.add_field(name="Region", value=server.region)
        embed.add_field(name="Created At", value=server.created_at.strftime("%Y-%m-%d"))
        await ctx.send(embed=embed)

    @commands.command(name='userinfo', description="Displays information about a user.")
    async def userinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(title=f"{member.display_name} Info", color=0x00ff00)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined At", value=member.joined_at.strftime("%Y-%m-%d"))
        embed.add_field(name="Roles", value=", ".join([role.name for role in member.roles[1:]]) or "None")
        await ctx.send(embed=embed)

    @commands.command(name='roles', description="Lists all server roles.")
    async def roles(self, ctx):
        roles = ctx.guild.roles
        role_names = ", ".join([role.name for role in roles if role.name != "@everyone"])
        await ctx.send(f"Roles: {role_names or 'None'}")

    @commands.command(name='invite', description="Generates an invite link for the server.")
    async def invite(self, ctx):
        invite_link = await ctx.channel.create_invite(max_age=300)
        await ctx.send(f"Invite link: {invite_link}")

    @commands.command(name='feedback', description="Sends feedback.")
    async def feedback(self, ctx, *, feedback):
        await ctx.send(f"Feedback received: {feedback}")

    @commands.command(name='emoji', description="Shows a set of emojis.")
    async def emoji(self, ctx):
        await ctx.send("Here are some emojis: 😊😢😂🔥👍")

    @commands.command(name='rules', description="Displays server rules.")
    async def rules(self, ctx):
        rules = "1. Be respectful.\n2. No spamming.\n3. No harassment."
        await ctx.send(rules)

    @commands.command(name='say', description="Repeats the message.")
    async def say(self, ctx, *, message):
        await ctx.send(message)

    @commands.command(name='choose', description="Randomly chooses an option from given choices.")
    async def choose(self, ctx, *, choices: str):
        choices_list = choices.split(',')
        choice = random.choice(choices_list).strip()
        await ctx.send(f"I choose: {choice}")

    @commands.command(name='fortune', description="Gives a random fortune.")
    async def fortune(self, ctx):
        fortunes = [
            "Good luck is coming your way!",
            "You will find a new hobby!",
            "An exciting opportunity awaits you!"
        ]
        await ctx.send(random.choice(fortunes))

    @commands.command(name='echo', description="Echoes back the message.")
    async def echo(self, ctx, *, message):
        await ctx.send(message)

    @commands.command(name='howdy', description="Sends a friendly greeting.")
    async def howdy(self, ctx):
        await ctx.send("Howdy, partner!")

    @commands.command(name='greeting', description="Sends a general greeting.")
    async def greeting(self, ctx):
        await ctx.send("Hello! How can I assist you today?")

    @commands.command(name='welcome', description="Welcomes new members.")
    async def welcome(self, ctx):
        await ctx.send("Welcome to the server!")

    @commands.command(name='goodbye', description="Says goodbye to members.")
    async def goodbye(self, ctx):
        await ctx.send("Goodbye! See you next time!")

    @commands.command(name='support', description="Provides support information.")
    async def support(self, ctx):
        await ctx.send("For support, please contact an admin.")

    @commands.command(name='version', description="Displays bot version.")
    async def version(self, ctx):
        await ctx.send("Bot version: 1.0.0")

    @commands.command(name='contact', description="Information on how to contact the bot team.")
    async def contact(self, ctx):
        await ctx.send("You can contact us via DM or by reaching out to the admins.")

    @commands.command(name='botinfo', description="Information about the bot.")
    async def botinfo(self, ctx):
        await ctx.send("I am a helpful bot created to assist you!")

    @commands.command(name='serverstats', description="Displays server statistics.")
    async def serverstats(self, ctx):
        server = ctx.guild
        await ctx.send(f"Server: {server.name}\nMember Count: {server.member_count}")

    @commands.command(name='membercount', description="Displays the number of members in the server.")
    async def membercount(self, ctx):
        member_count = ctx.guild.member_count
        await ctx.send(f"Total Members: {member_count}")

    @commands.command(name='channelinfo', description="Shows information about the current channel.")
    async def channelinfo(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(title=f"{channel.name} Info", color=0x00ff00)
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Type", value=channel.type)
        await ctx.send(embed=embed)

    @commands.command(name='whois', description="Shows user ID and info.")
    async def whois(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(f"User ID: {member.id}\nUsername: {member.name}")

    @commands.command(name='avatar', description="Shows user's avatar.")
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(member.avatar_url)

    @commands.command(name='pingrole', description="Pings a specific role.")
    async def pingrole(self, ctx, role: discord.Role):
        await ctx.send(f"{role.mention} has been pinged!")

    @commands.command(name='reminder', description="Sets a reminder.")
    async def reminder(self, ctx, time: int, *, message):
        await ctx.send(f"Reminder set for {time} seconds.")
        await asyncio.sleep(time)
        await ctx.send(f"Reminder: {message}")

    @commands.command(name='translate', description="Translates text to a given language.")
    async def translate(self, ctx, language: str, *, text):
        # Dummy implementation for example
        await ctx.send(f"Translating '{text}' to {language}... (not implemented)")

    @commands.command(name='servericon', description="Displays server icon.")
    async def servericon(self, ctx):
        await ctx.send(ctx.guild.icon_url)

    @commands.command(name='suggest', description="Sends a suggestion.")
    async def suggest(self, ctx, *, suggestion):
        await ctx.send(f"Suggestion received: {suggestion}")

    @commands.command(name='bugreport', description="Sends a bug report.")
    async def bugreport(self, ctx, *, report):
        await ctx.send(f"Bug report received: {report}")

    @commands.command(name='tips', description="Provides tips for users.")
    async def tips(self, ctx):
        await ctx.send("Tip: Always be respectful to others!")

    @commands.command(name='countdown', description="Starts a countdown.")
    async def countdown(self, ctx, seconds: int):
        for i in range(seconds, 0, -1):
            await ctx.send(i)
            await asyncio.sleep(1)
        await ctx.send("Countdown finished!")

    @commands.command(name='dailyfact', description="Provides a random daily fact.")
    async def dailyfact(self, ctx):
        facts = [
            "Honey never spoils.",
            "Bananas are berries, but strawberries aren't.",
            "A day on Venus is longer than a year on Venus."
        ]
        await ctx.send(random.choice(facts))

    @commands.command(name='fact', description="Provides a random fact.")
    async def fact(self, ctx):
        facts = [
            "Octopuses have three hearts.",
            "The Eiffel Tower can be 15 cm taller during the summer.",
            "Avocados are toxic to birds."
        ]
        await ctx.send(random.choice(facts))

    @commands.command(name='announce', description="Sends an announcement.")
    async def announce(self, ctx, *, announcement):
        await ctx.send(f"Announcement: {announcement}")

    @commands.command(name='messagecount', description="Counts messages in the current channel.")
    async def messagecount(self, ctx):
        async for _ in ctx.channel.history(limit=None):
            message_count += 1
        await ctx.send(f"Total messages: {message_count}")

    @commands.command(name='check', description="Checks the bot's status.")
    async def check(self, ctx):
        await ctx.send("Bot is online!")

    @commands.command(name='currenttime', description="Displays the current time.")
    async def currenttime(self, ctx):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        await ctx.send(f"Current time: {current_time}")

    @commands.command(name='timezone', description="Displays the bot's timezone.")
    async def timezone(self, ctx):
        await ctx.send("Bot's timezone is IST.")

    @commands.command(name='alert', description="Sends an alert message.")
    async def alert(self, ctx, *, message):
        await ctx.send(f"Alert: {message}")

    @commands.command(name='announcements', description="Shows where to find announcements.")
    async def announcements(self, ctx):
        await ctx.send("Announcements can be found in the #announcements channel.")

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))
    print("GeneralCommands cog loaded.")


