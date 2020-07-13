from random import choice
from discord.ext import commands
from cogs.utilitron_housing import Housing

class Pathing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def lowerize(self, arg):
        return arg.lower()

    def allow_backtracking(self, backtrack):
        if len(backtrack) > 0:
            if backtrack[0].lower() == "backtrack" or backtrack[0].lower == "b":
                return True

        return False

    @classmethod
    async def delegated_send(cls, ctx, message):
        channel_result = Housing.get_botchannel(ctx)
        if channel_result[0]:
            #send to qualified channel in this guild/server
            await channel_result[1].send(message)
        else:
            #send in DM to message author
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(message)

    @commands.command("cpath")
    async def generateCardinalPathing(self, ctx, spaces: int, *backtrack):
        print(backtrack)
        can_backtrack = self.allow_backtracking(backtrack)

        directions = ["N", "S", "E", "W"]
        path = []
        for _ in range(spaces):
            chosen = choice(directions)
            if not can_backtrack:
                if chosen is "N" and "S" in directions:
                    directions.remove("S")
                elif chosen is "S" and "N" in directions:
                    directions.remove("N")
                elif chosen is "E" and "W" in directions:
                    directions.remove("W")
                elif chosen is "W" and "E" in directions:
                    directions.remove("E")
            path.append(chosen)
        response_str = f"Your {spaces}-length path is:\n\t{path}"
        await Pathing.delegated_send(ctx, response_str)

    @commands.command("opath")
    async def generateOrdinalPathing(self, ctx, spaces: int, *backtrack):
        can_backtrack = self.allow_backtracking(backtrack)

        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        path = []
        for _ in range(spaces):
            chosen = choice(directions)
            if not can_backtrack:
                pass
            path.append(chosen)
        response_str = f"Your {spaces}-length path is:\n\t{path}"
        await Pathing.delegated_send(ctx, response_str)
