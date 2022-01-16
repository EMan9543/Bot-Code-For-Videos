# Imports (DONT EDIT MIGHT BE USED IN A DIFF VIDEO!)
import discord
import os
import json
import re
from discord.ext import commands
#  Prefix (Edit PREFIX HERE With your prefix)
bot = commands.Bot(command_prefix = "PREFIX HERE")

#Bot Commands

@bot.command()
async def ping(ctx):
    await ctx.send("Pongity Pong!")

bot.run("TOKEN HERE")    
