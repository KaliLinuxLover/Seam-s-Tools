
import discord
import os
import requests
import json
from keep_alive import keep_alive
from discord.utils import get

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  activity = discord.Game(name="$help", type=3)
  await client.change_presence(status=discord.Status.online, activity=activity)
  print("Ready")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('$inspireme'):
    quote = get_quote()
    await message.channel.send(quote)
  if message.content.startswith('$help'):
    await message.channel.send("$hello - Have the bot say hi!                             $inspireme - Have the bot pull a random quote!                                         $twitch - Seamless' Twitch!                                                                     $youtube - Seamless's YouTube Channel!                                        $tiktok - Seamless's TikTok!        DM DeathChampion#0328 to suggest more commands! ")
  if message.content.startswith('$twitch'):
    await message.channel.send("Seamless RL's twitch is https://www.twitch.tv/seamless_rl")
  if message.content.startswith('$youtube'):
    await message.channel.send("Seamless RL's YouTube is https://www.youtube.com/channel/UCrT-QFvlJyEJKHLHucVrfGQ")
  if message.content.startswith('$tiktok'):
    await message.channel.send("Seamless RL's TikTok is https://www.tiktok.com/@seamless.rl")
  

keep_alive()
client.run(os.getenv('TOKEN'))