# commands/general.py
from discord.ext import commands
import discord

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', description="Kick a member from the server.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked for: {reason}')

    @commands.command(name='ban', description="Ban a member from the server.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned for: {reason}')

    @commands.command(name='unban', description="Unban a member from the server.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == member or user.id == member:
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name} has been unbanned.')
                return
        await ctx.send(f'User {member} not found in ban list.')

    @commands.command(name='mute', description="Mute a member.")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role is None:
            await ctx.send("Muted role not found. Please create a role named 'Muted'.")
            return
        await member.add_roles(muted_role)
        await ctx.send(f'{member} has been muted.')

    @commands.command(name='unmute', description="Unmute a member.")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role is None:
            await ctx.send("Muted role not found. Please create a role named 'Muted'.")
            return
        await member.remove_roles(muted_role)
        await ctx.send(f'{member} has been unmuted.')

    @commands.command(name='purge', description="Delete a number of messages.")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} messages have been deleted.', delete_after=5)

    @commands.command(name='lock', description="Lock a channel.")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Channel locked.")

    @commands.command(name='unlock', description="Unlock a channel.")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("Channel unlocked.")

    @commands.command(name='slowmode', description="Set slowmode for the channel.")
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f'Slowmode set to {seconds} seconds.')

    @commands.command(name='nickname', description="Change a member's nickname.")
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, nickname=None):
        await member.edit(nick=nickname)
        await ctx.send(f"Nickname for {member.mention} changed to {nickname}.")

    @commands.command(name='addrole', description="Add a role to a member.")
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"Added {role.name} to {member.mention}.")

    @commands.command(name='removerole', description="Remove a role from a member.")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"Removed {role.name} from {member.mention}.")
