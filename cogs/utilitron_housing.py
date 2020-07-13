from discord.ext import commands

class Housing(commands.Cog):
    botChannelMap = dict()
    def __init__(self, bot):
        self.bot = bot

    @classmethod
    def get_botchannel(cls, ctx):
        """
        Tupled result (has_bot_channel: bool, bot_channel: Channel[Noneable])
        """
        channel = (False, None)
        if ctx.guild.id in cls.botChannelMap:
            channel = (True, ctx.guild.get_channel(cls.botChannelMap[ctx.guild.id]))
        return channel

    def is_mod(ctx):
        return ctx.author.guild_permissions.manage_channels

    @commands.command()
    @commands.check(is_mod)
    async def homeis(self, ctx, *channel):
        if len(channel) == 0:
            channel = self.get_botchannel(ctx)
            if channel[0]:
                await channel[1].send("I have been instructed to remain in this location.")
            else:
                await ctx.send("I have not been designated a channel.")
        else:
            channel_id = None
            for text_channel in ctx.guild.text_channels:
                if text_channel.name == channel[0]:
                    channel_id = text_channel.id
                    break
            if channel_id == None:
                await ctx.send(f'Sorry, I don\'t see "{channel[0]}" in this server.')
            else:
                self.botChannelMap[ctx.guild.id] = channel_id
                response = ("Acknowledged: this is the "
                "home of bots in this server.")
                await ctx.guild.get_channel(channel_id).send(response)

    @commands.command()
    @commands.check(is_mod)
    async def homeishere(self, ctx):
        await self.homeis(ctx, ctx.channel.name)

    @commands.command()
    @commands.check(is_mod)
    async def evict(self, ctx):
        channel = self.get_botchannel(ctx)
        if channel[0]:
            response = f"Acknowledged: I have been evicted from {channel[1].name}."
            await channel[1].send(response)
        else:
            response = ("Impossible: I was not assigned a channel "
            "in this server in the first place.")
            await ctx.send(response)
