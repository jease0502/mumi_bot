#!/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from discord.ext import commands
from mongo.mongo import MongoDB
import discord


bot = commands.Bot(command_prefix='!')
intents = discord.Intents.default()
intents.members = True
db = MongoDB()

@bot.command()
async def DM(ctx, user: discord.User, message=None):
    message = "神奇卡牌"
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
    if message.content == '召喚卡牌':
        await DM(message.author, "msg")
    elif db.get_data(message.content) != False:
        print(db.get_data(message.content))
        await message.channel.send(db.get_data(message.content))
    # elif message.content.startswith('姆咪新增'):
    #     tmp = message.content.split(" ",3)
    #     if len(tmp) == 1:
    #         await message.channel.send("新增失敗")
    #     else:
    #         db.insert_data(tmp[1], tmp[2])
    #         await message.channel.send("新增成功")



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