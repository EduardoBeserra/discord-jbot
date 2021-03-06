import random
import googletrans
tradutor = googletrans.Translator()
translatorsrc = 'pt'
translatordest = 'en'

def apostamega(message):
    strret = message.author.name + '. Seus números da sorte: '
    for n in range(1, 7):
        strret += str(random.randint(1, 60))
        if n < 6:
            strret += ', '
    return strret


def msgesio(message):
    msg = []
    if 'marcio' in message.author.name.lower():
        msg = [
            'Aaaaah Marcio!',
            'https://i.imgur.com/ukg2aWT.jpg'
        ]
    else:
        msg = [
            'Testando som.... som... Josi... som.',
            'Va lavar as tetas com ki-suco.'
        ]
    return msg[random.randint(0, len(msg) - 1)]


def cigarroaleatorio(message):
    imgs = [
        'https://media.tenor.com/images/6b5623306a01f59c3db399cb5081c6ac/tenor.gif',
        'https://media.tenor.com/images/8a726f1ffcd640e212d8d01f0035f72d/tenor.gif',
        'https://media.tenor.com/images/6782d48e17a9b407c45e182ad095f89e/tenor.gif',
        'https://media.tenor.com/images/cc3e2c5d673b94ac7740a589ac7f6066/tenor.gif',
        'https://media.tenor.com/images/82454b048b6fad7a0414775738f884e0/tenor.gif',
        'https://media.tenor.com/images/5ed42e19153e45975ec65b474bc20cbf/tenor.gif',
        'https://media.tenor.com/images/e9c174e51cec099cc736f1de12b5c291/tenor.gif',
        'https://media.tenor.com/images/3f0e8c7e834135611b1fbae108fe527f/tenor.gif',
        'https://media.tenor.com/images/e0453ca8758ae8f9687e0359f41cdc82/tenor.gif',
        'https://media.tenor.com/images/d77f7f76b792d4c16bb494e04d84880b/tenor.gif',
        'https://i.imgur.com/TvQUGtl.jpg'
    ]
    return imgs[random.randint(0, len(imgs) - 1)]


def traduzir(message):
    texto = message.content.replace("-josi", "").replace("traduz", "")
    return tradutor.translate(texto, src=translatorsrc, dest=translatordest).text

def setidiomas(message):
    global translatorsrc, translatordest
    txt = message.content.replace("-josi", "").replace("idioma", "").replace("de:", "")
    arr = txt.split("para:")
    if len(arr) >= 2:
        translatorsrc = arr[0].strip()
        translatordest = arr[1].strip()
        return "feito!"
    else:
        return "Não entendi {}.".format(message.author.name)

def wiki(message):
    if 'ireport' in message.content:
        return '''
Você vai precisar dessas libs:
https://i.imgur.com/bib6Goa.png
Adiciona elas no classpath e configura desta forma:
https://i.imgur.com/eSK58U3.png
'''
    if ' infra ' in message.content:
        return 'http://infraestrutura.datacoper.com.br/Login.aspx'
    if 'deploy' in message.content:
        return '''
Comando para fazer undeploy:
/u01/integradorprogress/glassfish4/bin/asadmin --port=4848 undeploy IntegradorProgress
Comando para fazer deploy:
/u01/integradorprogress/glassfish4/bin/asadmin --port=4848 deploy --name IntegradorProgress IntegradorProgress.war
'''

        
comandos = {
    'linkhomer': 'http://10.30.5.16:3000',
    'avatar': 'https://i.imgur.com/YH54Rhx.jpg',
    'burgman': 'https://i.imgur.com/KoFRE5R.jpg',
    'fast': 'https://runitwice.files.wordpress.com/2017/09/flash-slowmo-joke-small-preguic3a7a-poker.gif',
    'compilar': 'https://static.globalnoticias.pt/storage/DN/2016/original/ng7559622.jpg',
    'goleiro': 'https://i.imgur.com/5uWKkPy.gifv',
    'ciclista': 'https://i.imgur.com/K4jgGWB.png',
    'ahmarcio': 'https://i.imgur.com/ukg2aWT.jpg'
}
funcoes = {
    'megasena': apostamega,
    'cigarro': cigarroaleatorio,
    'msgesio': msgesio,
    'traduz': traduzir,
    'idioma': setidiomas,
    'wiki': wiki
}