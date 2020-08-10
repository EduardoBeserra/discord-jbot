import discord
import asyncio, json, time
from comandos import comandos, funcoes

clientId = ''
with open('clientId.json', 'r') as f:
    clientId = json.load(f)['clientId']
    f.close()
client = discord.Client()

@client.event
async def on_ready():
    print('Opa, iniciei!')
    print(client.user.id, client.user.name)

@client.event
async def on_message(message):
    if message.content.lower().startswith('-josi'):
        nenhum_retorno = True
        if 'help' in message.content.lower():
            strcom = ''
            for c in comandos.keys():
                strcom += c + '\n'
            for f in funcoes.keys():
                strcom += f + '\n'
            await message.channel.send(strcom)
            nenhum_retorno = False
        else:
            com = message.content[5:].strip().lower()
            if com in comandos:
                await message.channel.send(comandos[com])
                nenhum_retorno = False
            elif com in funcoes:
                await message.channel.send(funcoes[com](message))
                nenhum_retorno = False
        if nenhum_retorno:
            await message.channel.send(funcoes['msgesio'](message))
    else:
        com = message.content.lower()
        if 'kkkkk' in com or 'haha' in com:
            time.sleep(10)
            await message.channel.send('https://tenor.com/view/laugh-zootopia-smile-sarcasm-sloth-gif-5358369')

client.run(clientId)