import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("알림장봇")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("1반"):
        await message.channel.send("?")

    if message.content.startswith("사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

client.run("OTUxNzMxNDA5ODUxMTI5OTA2.Yiru8g.imAkRdqq8XZEooeXJ_YVHeaaIeM")




