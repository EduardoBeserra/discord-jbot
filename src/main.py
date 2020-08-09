import discord
import asyncio, json

clientId = ''
with open('clientId.json', 'r') as f:
    clientId = json.load(f)['clientId']
    f.close()
client = discord.Client()

@client.event
async def on_ready():
    print('Opa, bom dia. Eu sou o {}'.format(client.user.name))
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.lower().startswith('-josi'):
        nenhum_retorno = True
        if 'avatar' in message.content.lower():
            await message.channel.send('https://drive.google.com/file/d/1jOVM1iT5xIT4ZpDf3cuC2mcctjEyIL54/view?usp=sharing')
            nenhum_retorno = False

        if nenhum_retorno:
            await message.channel.send('Testando som.... som... Josi... som.')

client.run(clientId)