import discord
import os
import openpyxl 
from deep_translator import GoogleTranslator

client = discord.Client()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        text="In the first line, you have to write the language that is your input word and the language that you want to be your output like this: \n en fr \n In the second line, you must write the sentence you want to translate like this: \n hi world"
        await message.channel.send(text)


    elif message.content.startswith(''):
        my_string=message.content
        first = my_string.split('\n', 1)[0]
        second_line = my_string.split('\n', 1)[1]


        N = 0
        count = 0
        secondlang = ""
        for ele in first:
            if ele == ' ':
                count = count + 1
                if count == N:
                    break
                secondlang = ""
            else :
                secondlang = secondlang + ele


        Nn = 1
        coun = 0
        firstlang = ""
        for el in first:
            if el == ' ':
                coun = coun + 1
                if coun == Nn:
                    break
                firstlang = ""
            else :
                firstlang = firstlang + el

        translated = GoogleTranslator(source=firstlang, target=secondlang).translate(second_line)  # output -> Weiter so, du bist großartig

        await message.channel.send(translated)

client.run(TOKEN)


