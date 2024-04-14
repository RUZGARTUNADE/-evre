import discord 
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptık.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("BAY")
    elif message.content.startswith('+no.1best'):
        await message.channel.send("Sago daha iyi")
    elif message.content.startswith('$çevreoyunu'):
        await message.channel.send("%selam dostum,hangi ev eşyasının doğada kaç yılda kaybolduğunu öğrenmek istersin?(pil,strafor,plastik,cam şişe):")
    elif message.content.startswith('$çevreoyunu.pil'):
        await message.channel.send("300 yıl(çok fazla demi bu daha ne ki )")
    elif message.content.startswith('$çevreoyunu.strafor'):
        await message.channel.send("5000 yıl - 2 Milyon yıl(öfff)")
    elif message.content.startswith('$çevreoyunu.plastik'):
        await message.channel.send("1000 yıl(bence sakın plastiği çöpe atma)")
    elif message.content.startswith('$çevreoyunu.camşişe'):
        await message.channel.send("4000 yıl(şaşırdın demi bende çok şaşııryorum.)")
    
bot.run("MTIyMTQ4NjA5NTI4MDI0NjgzNA.GWKjnu.KgNeO-xdZsyMs4EOBW2wpihNpM6g0JHoL9CFvg")