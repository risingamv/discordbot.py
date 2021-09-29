import discord
from discord.ext import commands

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

client.run("TOKEN") 
