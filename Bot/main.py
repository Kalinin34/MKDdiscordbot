
import discord
import TokenParser


client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print("Бот Активный - {0.user}".format(client))


@client.event
async def on_message(message: discord.Message):
    if message.type == discord.MessageType.new_member:
        member = message.author
        role = discord.utils.get(message.guild.roles,name=TokenParser.getDefaultRole())
        await member.add_roles(role)


client.run(TokenParser.getTOKEN())