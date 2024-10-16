# economy.py
from discord.ext import commands
import discord
import random
import pymongo
from config import MONGODB_URL
from datetime import datetime, timedelta
import asyncio
import emoji  # Import your emoji file

# MongoDB setup
client = pymongo.MongoClient(MONGODB_URL)
db = client['economy']  # Database name
users_collection = db['users']  # Collection name

class EconomyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # MongoDB setup
        self.client = pymongo.MongoClient(MONGODB_URL)
        self.db = self.client['economy']  # Database name
        self.users_collection = self.db['users']  # Collection name
        print("\033[92mConnected to MongoDB!\033[0m")  # Notify in the console
        
    async def get_user_data(self, user_id):
        user = users_collection.find_one({"user_id": user_id})
        if user is None:
            users_collection.insert_one({"user_id": user_id, "balance": 0, "last_daily": None, "last_weekly": None, "last_monthly": None})
            return {"user_id": user_id, "balance": 0, "last_daily": None, "last_weekly": None, "last_monthly": None}
        return user

    @commands.command(name='balance', description="Check your balance.")
    async def balance(self, ctx):
        user_data = await self.get_user_data(ctx.author.id)
        await ctx.send(f"Your balance is {user_data['balance']} {emoji.BANK_EMOJI}")

    @commands.command(name='search', description="Search for some money.")
    async def search(self, ctx):
        found_money = random.randint(1, 100)
        user_data = await self.get_user_data(ctx.author.id)
        users_collection.update_one({"user_id": ctx.author.id}, {"$set": {"balance": user_data["balance"] + found_money}})
        await ctx.send(f"You found {found_money} {emoji.BANK_EMOJI}! Your new balance is {user_data['balance'] + found_money} {emoji.BANK_EMOJI}")

    @commands.command(name='work', description="Work to earn some money.")
    async def work(self, ctx):
        await ctx.send("You are working...")
        await asyncio.sleep(5)  # Simulate work time
        earned_money = random.randint(10, 50)
        user_data = await self.get_user_data(ctx.author.id)
        users_collection.update_one({"user_id": ctx.author.id}, {"$set": {"balance": user_data["balance"] + earned_money}})
        await ctx.send(f"You earned {earned_money} {emoji.BANK_EMOJI}! Your new balance is {user_data['balance'] + earned_money} {emoji.BANK_EMOJI}")

    @commands.command(name='transfer', description="Transfer money to another user.")
    async def transfer(self, ctx, member: discord.Member, amount: int):
        if amount <= 0:
            await ctx.send("You cannot transfer a negative or zero amount.")
            return
        sender_data = await self.get_user_data(ctx.author.id)
        if sender_data['balance'] < amount:
            await ctx.send("You do not have enough balance.")
            return
        recipient_data = await self.get_user_data(member.id)
        users_collection.update_one({"user_id": ctx.author.id}, {"$set": {"balance": sender_data["balance"] - amount}})
        users_collection.update_one({"user_id": member.id}, {"$set": {"balance": recipient_data["balance"] + amount}})
        await ctx.send(f"You transferred {amount} {emoji.BANK_EMOJI} to {member.mention}. Your new balance is {sender_data['balance'] - amount} {emoji.BANK_EMOJI}")

    @commands.command(name='daily', description="Claim your daily reward.")
    async def daily(self, ctx):
        user_data = await self.get_user_data(ctx.author.id)
        now = datetime.now()
        if user_data['last_daily'] is not None and now - user_data['last_daily'] < timedelta(days=1):
            await ctx.send("You can claim your daily reward only once every 24 hours.")
            return
        reward = 100  # Fixed daily reward
        users_collection.update_one({"user_id": ctx.author.id}, {"$set": {"balance": user_data["balance"] + reward, "last_daily": now}})
        await ctx.send(f"You claimed your daily reward of {reward} {emoji.BANK_EMOJI}! Your new balance is {user_data['balance'] + reward} {emoji.BANK_EMOJI}")

    @commands.command(name='weekly', description="Claim your weekly reward.")
    async def weekly(self, ctx):
        user_data = await self.get_user_data(ctx.author.id)
        now = datetime.now()
        if user_data['last_weekly'] is not None and now - user_data['last_weekly'] < timedelta(weeks=1):
            await ctx.send("You can claim your weekly reward only once every 7 days.")
            return
        reward = 500  # Fixed weekly reward
        users_collection.update_one({"user_id": ctx.author.id}, {"$set": {"balance": user_data["balance"] + reward, "last_weekly": now}})
        await ctx.send(f"You claimed your weekly reward of {reward} {emoji.BANK_EMOJI}! Your new balance is {user_data['balance'] + reward} {emoji.BANK_EMOJI}")

    @commands.command(name='monthly', description="Claim your monthly reward.")
    async def monthly(self, ctx):
        user_data = await self.get_user_data(ctx.author.id)
        now = datetime.now()
        if user_data['last_monthly'] is not None and now - user_data['last_monthly'] < timedelta(days=30):
            await ctx.send("You can claim your monthly reward only once every 30 days.")
            return
        reward = 2000  # Fixed monthly reward
        users_collection.update_one({"user_id": ctx.author.id}, {"$set": {"balance": user_data["balance"] + reward, "last_monthly": now}})
        await ctx.send(f"You claimed your monthly reward of {reward} {emoji.BANK_EMOJI}! Your new balance is {user_data['balance'] + reward} {emoji.BANK_EMOJI}")

