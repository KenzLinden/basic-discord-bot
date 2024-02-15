import subprocess
import psutil
import servers
import discord
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')




def handle_response(message) -> str:
    p_message = message.lower()
    
    # palworld commands
    if p_message == '*close':
        print("Closing palworld!")
        if(servers.end_palworld_server() == 1):
            return("PalWorld server closed!")
        else:
            return("Server is already closed!")
    
    if p_message == '*open':
        if("PalServer-Win64-Test-Cmd.exe" in (p.name() for p in psutil.process_iter())):
            return('Server is already open on IP: ' + str(ip) + "!")
        else:
            servers.start_palworld_server()
            return("PalWorld server now open! Join on IP: " + str(ip) + ":8211")
    
    
    
    # general commands

    if p_message == '*fart':
        return "Excuse you!"
    
  
        
    
    
    
    