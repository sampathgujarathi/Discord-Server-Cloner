mytitle = "Lua Cloner - Developed by G∙MAX#1122"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

bot = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

                            ██╗░░░░░██╗░░░██╗░█████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                            ██║░░░░░██║░░░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                            ██║░░░░░██║░░░██║███████║  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
                            ██║░░░░░██║░░░██║██╔══██║  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
                            ███████╗╚██████╔╝██║░░██║  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
                            ╚══════╝░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                                                    {Fore.MAGENTA}Developed by: Sampath#1952.{Style.RESET_ALL}
        """)
token = input(f'Please enter your account token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your token


print("  ")
print("  ")

@bot.event
async def on_ready():
    print("Loading...")
    time.sleep(2)
    extrem_map = {} 
    print(f"Logged In as : {bot.user}")
    print("Cloning Server")
    guild_from = bot.get_guild(int(input_guild_id))
    guild_to = bot.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    await Clone.emojis_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


                                        ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                        ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                        ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                        ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                        ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                        ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    


bot.run(token, bot=False)