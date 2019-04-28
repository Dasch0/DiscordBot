import discord

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.conent == '!test':
            await message.channel.send('test')

client = MyClient()
client.run('NTcxODc1MDI1MjE3Mzg4NTQ0.XMUR7w.RPtja4qv5fjbd4nDGPC78T-fQNg')
