import discord
import commands



FUNCTION_CHANNEL = 1051735080294432838

async def run_command(message, user_message):
    try:
        response = await commands.handle_response(message, user_message)
        #await message.channel.send(response)
    except Exception as e:
        print(e)
        

def run_discord_bot():
    with open('token.txt') as f:
        DISCORD_TOKEN = f.readline()

    bot_intents=discord.Intents.default()
    bot_intents.message_content = True
    client = discord.Client(intents=bot_intents)
    
    @client.event
    async def on_ready():
        print("Bot is now running")
        channel = client.get_channel(FUNCTION_CHANNEL)
        await channel.send("Sphincter is now awake!")
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        await run_command(message, user_message)
        print(username + " used message " + user_message  + " ")
        
        
    client.run(DISCORD_TOKEN)
        