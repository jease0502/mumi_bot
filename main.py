#!/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from discord.ext import commands
import discord


bot = commands.Bot(command_prefix='!')
intents = discord.Intents.default()
intents.members = True

@bot.command()
async def DM(ctx, user: discord.User, message=None):
    message = message or "This Message is sent via DM"
    print("message" , message)
    await ctx.send(message)

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    game = discord.Game('努力幫斯養貓咪')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event    
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('姆咪'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("姆咪？？？")
        else:
            await message.channel.send(tmp[1])
    if message.content == '瞅啥瞅？':
        await DM(message.author, "瞅啥瞅？")
    elif message.content == '嗚嗚嗚':
        await message.channel.send("嗚嗚嗚摸摸頭！")
    elif '小斯' in message.content:
        await message.channel.send("找主人嗎？")
    elif '午安咪姆' in message.content:
        await message.channel.send("都不跟我說的嗎？")
    elif '午安姆咪' in message.content:
        await message.channel.send("午安安～")
    elif '咪姆好可愛' in message.content:
        await message.channel.send("嗯？\n我也很可愛！")
    elif '咪姆我要抽扭蛋' in message.content:
        await message.channel.send("扭屁扭！")


    if message.content.startswith('更改狀態'):
        #切兩刀訊息
        tmp = message.content.split(" ",2)
        #如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await bot.change_presence(status=discord.Status.idle, activity=game)

if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('discord_token')
    bot.run(token)