#!/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from server import MyClient
import discord


client = discord.Client()
@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    game = discord.Game('努力幫斯養貓咪')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event    
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('姆咪'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("姆咪？？？")
        else:
            await message.channel.send("姆咪？？？")
    if message.content == 'ping':
        await message.channel.send('pong')


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('discord_token')
    client.run(token)