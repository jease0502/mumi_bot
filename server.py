import discord

class MyClient(discord.Client):
    client = discord.Client()
    def __init__(self,discord_token):
        self.token = discord_token

    @client.event
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        game = discord.Game('努力幫斯養貓咪')
        await self.client.change_presence(status=discord.Status.idle, activity=game)

    @client.event    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('姆咪'):
            tmp = message.content.split(" ",2)
            if len(tmp) == 1:
                await message.channel.send("姆咪？？？")
            else:
                await message.channel.send("姆咪？？？")
        if message.content == 'ping':
            await message.channel.send('pong')