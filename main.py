import discord

client = discord.Client()
print("""
  ___ _            _       __  __              ___  __  __            
 / __(_)_ __  _ __| |___  |  \/  |__ _ ______ |   \|  \/  |           
 \__ \ | '  \| '_ \ / -_) | |\/| / _` (_-<_-< | |) | |\/| |           
 |___/_|_|_|_| .__/_\___| |_|  |_\__,_/__/__/ |___/|_|  |_|           
       _ _   |_|      _                     __                        
  __ _(_) |_| |_ _  _| |__   __ ___ _ __   / / _  _____ _____ _ _  ___
 / _` | |  _| ' \ || | '_ \_/ _/ _ \ '  \ / / ' \/ -_) \ / _ \ ' \(_-<
 \__, |_|\__|_||_\_,_|_.__(_)__\___/_|_|_/_/|_||_\___/_\_\___/_||_/__/
 |___/                     
 
 https://github.com/nexons/massdm                                           
""")
token = input("Input your token: ")

@client.event
async def on_connect():
  msg = input("Enter message to MASSDM: ")
  for user in client.user.friends:
    try:
       await user.send(msg)
       print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run(token, bot=False)
   