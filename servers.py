#PALWORLD
import subprocess
import psutil
import discord


def start_palworld_server():
        subprocess.Popen(['D:\SteamLibrary\steamapps\common\PalServer\PalServer.exe'])
        return("PalWorld server now open")


def end_palworld_server():
    if not 'PalServer-Win64-Test-Cmd.exe' in (p.name() for p in psutil.process_iter()):
        return 0
    subprocess.call("TASKKILL /IM PalServer-Win64-Test-Cmd.exe")
    return 1
    
