import discord
from discord.ext import commands, tasks
from discord import message
import random
import os
from discord.utils import get
from itertools import cycle
import asyncio
from  discord import guild
import time

intents = discord.Intents(messages = True, guilds = True, members = True)
client = commands.Bot(command_prefix = '.', intents=intents)

#! on ready
@client.event
async def on_ready():
    activity = discord.Activity(name='SERVER', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    for x in client.guilds:
        print(f"=== BOT IS READY ON : {x.name}")

#! on member join
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

#! on member remove 
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

#! .ping
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
    write("ping")

#! .credits
@client.command()
async def credits(ctx):
    await ctx.send("```Made by - Rozbita_Zaluzie```")
    await ctx.send("```IG - https://www.instagram.com/rozbita_zaluzie/```")
    write("credits")

#* .pilot
@client.command()
async def pilot(ctx):
    responses = ["I will be Pilot and destroy India!!!"]
    await ctx.send(f'{random.choice(responses)}')
    write("pilot")

#* .pele
@client.command()
async def pele(ctx):
    leng = ['mm','cm','m']
    x = random.randint(0,100)
    xx = random.choice(leng)
    if x % 11 == 0:
        await ctx.send('404 - Tvoje pelko not found')
    elif x % 15 == 0:
        await ctx.send('you mother small')
    else:
        await ctx.send(f'Tvoje pelko má {x} {xx}')
    write("pele")

#* .anone
@client.command()
async def anone(ctx, *, question):
    responses = ["Samozřejmě", "Ano", "Možná", "Ne", "Ani náhodou :|"]
    await ctx.send(f'Otázka: {question}\nOdpověd: {random.choice(responses)}')
    write("anone")
    
#* .jakoty
@client.command()
async def jakoty(ctx):
    responses = ["Maximálně ty", "Maska jaska", "Jaska fiska", "Míla íla","you mother small" , "knedl :|", "Minimálně ty", "Průměrně ty", "Jako já"]
    await ctx.send(f'{random.choice(responses)}')
    write("jakoty")

#* .kralik
@client.command()
async def kralik(ctx):
    responses = ["Měl by si ho nakrmit", "Ty prasa zoofilské", "Ferda :D", "Celkem fešný bobek"]
    await ctx.send(f'{random.choice(responses)}')
    write("kralik")

#* .didorici
@client.command()
@commands.has_any_role("Majitel", "Admin")
async def didorici(ctx):
    await ctx.send("Omlouvám se mistře, tato chyba se už nebude opakovat")
    write("didorici")

#! .trello
@client.command()
async def trello(ctx):
    await ctx.send("Tello - ")
    write("trello")

#! .join
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    write("join")
   
#! .leave
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    write("leave")

#! .members
@client.command()
async def members(ctx):
    await ctx.send(f"This server has {ctx.guild.member_count} members.")
    i = 0
    for x in ctx.guild.members:
        await ctx.send(f"`{i}. - {x.name}`")
        i+=1
    write("members")

#* .facka
@client.command()
async def facka(ctx):
    lis = []
    
    for x in ctx.guild.members:
        lis.append(x)
    
    r = random.choice(lis)
    if r == ctx.author:
        await ctx.send(f"{r.mention} si dal facku... (proč se mlátíš ty buzno ??)")
    else: 
        odpovedi = [" dostal facku od "," dostal granáta od "," byl proplesknut "]
        slovo = random.choice(odpovedi)

        await ctx.send(f"{r.mention}{slovo}{ctx.author.mention}")
    write("facka")

#? .lock
@client.command()
async def lock(ctx, member: discord.Member, channel : discord.VoiceChannel):
    start_time = time.time()
    t_end = start_time + 30
    i = 0
    while time.time() < t_end:
        try:
            await member.move_to(channel)
        except:
            print("idiote")
        print(i)
        i+=1
        time.sleep(0.1)

#* .meme
@client.command()
async def meme(channel):
    imgs = []
    with os.scandir('memes/') as memes:
        for image in memes:
            imgs.append(image) 
    meme = random.choice(imgs)
    memeC = "memes\\" + str(meme.name) 
    await channel.send(file=discord.File(memeC))

#// write stats
def write(commandN):
    print("added --> " + commandN)
    fileR = open("stats.txt", "r")
    stats = []
    for x in fileR:
        if x.startswith(commandN):
            st = x.split(" - ")
            i = int(st[1])
            i+=1
            x = st[0] + " - " + str(i) + "\n"
        stats.append(x)
    with open('stats.txt', 'w') as file2:
        file2.writelines( stats )    

tokenF = open("token.txt", "r")
token = tokenF.readline()
client.run(token)
