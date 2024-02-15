import subprocess
import psutil
import servers
import discord
from requests import get
import sys
import CONSTANTS

ip = get('https://api.ipify.org').content.decode('utf8')




async def handle_response(message_obj, user_message):
    p_message = user_message.lower()
    
    # minecraft server commands
    
    
    # REMOVED BECAUSE YOU CANNOT TRUST ANYONE IN POOLS CLOSED
    # if p_message == '*close':
    #    print("Closing palworld!")
    #    if(servers.end_minecraft_server() == 1):
    #        await message_obj.channel.send("PalWorld server is now closed!")
    #        return 1
    #    else:
    #        await message_obj.channel.send("PalWorld server is already closed!")
    #        return 1
    
    if p_message == '*open':
        if(CONSTANTS.PROGRAM_NAME in (p.name() for p in psutil.process_iter())):
            await message_obj.channel.send("Minecraft server is already open on IP: " + str(ip) + ":8211")
            return 1
        else:
            servers.start_minecraft_server()
            await message_obj.channel.send("Minecraft server now open! Join on IP: " + str(ip) + ":8211")
            return 1
    
    
    
    # # general commands
    
    # if p_message == "*die":
    #     await message_obj.channel.send("Bot out! Goodbye!")
    #     sys.exit()

    # if p_message == '*fart':
    #     await message_obj.channel.send("Excuse you!")
    #     return 1
    
  
        
    
    
    
    