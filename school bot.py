import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("1반"):
        await message.channel.send("ㅇㅇ")
    
    if message.content.startswith("뭐해"):
        await message.channel.send("니생각")

    if message.content.startswith("사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)




