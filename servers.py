#PALWORLD
import subprocess
import psutil
import discord
import CONSTANTS

# !!!PUT DIRECTORY FOR SERVERS HERE!!!


def start_palworld_server():
        subprocess.Popen([CONSTANTS.SERVER_DIRECTORY])
        return("Minecraft server now open")


def end_minecraft_server():
    if not CONSTANTS.PROGRAM_NAME in (p.name() for p in psutil.process_iter()):
        return 0
    subprocess.call("TASKKILL /IM " + CONSTANTS.PROGRAM_NAME)
    return 1
    
