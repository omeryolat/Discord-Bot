import discord
from discord.ext import commands
from utils import *
from veriler import getInfo
import random
intents = discord.Intents.all()
client=discord.Client(intents=intents)
channel=None
msg=None
users=[]

@client.event
async def on_reaction_add(reaction, user):
    global channel,msg
    if(channel is not None and msg is not None):
        if reaction.message.channel.id == channel.id:
            if reaction.emoji == '🎉':
                async for usr in reaction.users():
                    users.append(usr)

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    ctx=str(message.content).strip()
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    if(ctx[0]=="+"):
        if ctx== '+99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

        elif ctx == '+info':
            count=0
            for member in client.get_all_members():
                if str(member.status)!='offline':
                    count+=1
            await message.channel.send("------**`"+message.guild.name+
            "`**------\n\n:pushpin: **Total Members**: **`"+str(len(client.users))+"`**\n\n"+
            ":white_check_mark: **Online Members:** **`"+str(count)+"`**")

        elif ctx == '+ping':
            await message.channel.send("<@"+str(message.author.id)+"> :point_right: pong...")

        elif ctx == '+delete':
            await discord.TextChannel.purge(message.channel,limit=20)

        elif ctx == '+space':
            text=""
            for i in range(50):
                text+="\n᲼᲼᲼᲼᲼᲼"
            await message.channel.send(text)  

        elif ctx == '+connect':
            await message.author.voice.channel.connect()

        elif ctx == '+disconnect':
            for x in client.voice_clients:
                    return await x.disconnect()

            return await message.channel.send(":x: **I am not connected to any voice channel on this server!**")

        elif ctx=='+draw start':
            global channel,msg
            if(len(users)==0):
                await message.channel.send(":tada: **Draw Starting!**")
                channel=await client.fetch_channel(message.channel.id)
                msg=await channel.fetch_message(channel.last_message_id)
                await msg.add_reaction('🎉')
            else: 
                await message.channel.send(":x: **Draw already started! (`+draw finish` for finish it)**")

        elif ctx=='+draw finish':
            if len(users)>1:
                key=True
                while(key):
                    winner=random.choice(users)
                    if(winner.name!=client.user.name):
                        await message.channel.send(":confetti_ball: **Winner is ** <@"+str(winner.id)+">!")
                        key=False
                users.clear()
            elif len(users)==1:
                await message.channel.send(":thinking: **Winner is! ME** `No any participant for draw` ")
                users.clear()
            else:
                await message.channel.send(":x: **There is no any started draw! (`+draw start` for start it)**")


        elif ctx.__contains__('+lol'):
            value=getInfo(ctx.split('lol')[1].strip())
            if value==0:
                await message.channel.send(':face_with_monocle: **Summoner Cannot Found !**')
            else:
                await message.channel.send(
                "\U0001F977 **Username:** **`"+value[0]+
                "`**\n\n\U0001F4AA **Level:** **`"+value[1]+
                "`**\n\n\U0001F5E1 **SoloQ Rank:** **`"+value[2]+" - "+value[3]+
                "`**\n\n:crossed_swords: **Flex Rank:** **`"+value[4]+" - "+value[5]+"`**")
        else:
            await message.channel.send(":x: **There is no such command ! \nUsage `+command name`**")

client.run(TOKEN)
