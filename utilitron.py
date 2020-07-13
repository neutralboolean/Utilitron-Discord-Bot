import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs.utilitron_randpath import Pathing
from cogs.utilitron_housing import Housing
from random import random
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=commands.when_mentioned)
bot.add_cog(Pathing(bot))
bot.add_cog(Housing(bot))

async def is_owner(ctx):
    return ctx.author.id == bot.owner_id

@bot.event
async def on_ready():
    ready = "||THIS IS A UTILITY TO GENERATE VALID, RANDOM DIRECTIONS FOR\
    TERRAIN PLACEMENT IN BOARD GAMES WITH CARDINAL DIRECTIONS||"
    print(ready)


@bot.command()
async def ping(ctx):
    channel_result = Housing.get_botchannel(ctx)
    pong = f"pong: {bot.latency} ms"
    if channel_result[0]:
        await channel_result[1].send(pong)
    else:
        await ctx.send(pong)

@bot.command()
@commands.is_owner()
async def die(ctx):
    print("Leaving servers...")
    if random() > 0.95:
        await ctx.send("http://www.willtheterminatorcometrue.com/wp-content/uploads/2015/12/terminator-ill-be-back.gif")
    await bot.logout()


bot.run(TOKEN)
