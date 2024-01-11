import webbrowser
import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import re
import sys
import shutil
import keyboard
import time

def print_horizontal_line():
    terminal_width, _ = shutil.get_terminal_size()
    print('-' * terminal_width)

# Redirect stdout and stderr to a file
sys.stderr = open('bot_errors.log', 'w')


print(f'+----------------------------------------------------------------------+')
print(f'        DO NOT FORGET TO CHANGE THE PREFERRED BROWSER TO DEFAULT       ')
print(f'+----------------------------------------------------------------------+')
print('CC: cleary#6546 / @preorderd')
print('Moded by Anish Budha')
print_horizontal_line()



client = Bot('adawd@@#^^')
client.remove_command('help')

token = input("Please enter the discord token: ")

#enter channel id(s) where links would be picked up (monitor channel id) seperated by commas. these should be ints
channel_ids_input = input("Enter channel IDs separated by space: ")
channels = [int(channel_id) for channel_id in channel_ids_input.split()]

#prompt user enter keywords to check for in links
keywords = list(map(str,input("Enter keywords seperated by space: ").split()))

#prompt user to enter negative keywords that will prevent a browser window from opening to have no blacklisted words, press enter right away
blacklist = list(map(str,input("Enter blacklisted keywords seperated by space: ").split()))



#enter token of discord account that has access to watch specified channels

global start_count
start_count = 0


#check for keywords and blacklisted words in message urls and open browser if conditions are met
async def check_urls(urls):
    for url in urls:
        if any(x in url.lower() for x in keywords) and all(x not in url.lower() for x in blacklist):
            #enter path to chrome here, for windows 10, this should work
            webbrowser.open_new(url)
            print_horizontal_line()
            print(f'Opened: {url}')
            print_horizontal_line()

print("Starting", end="", flush=True)
for _ in range(5):
    time.sleep(1)
    print(".", end="", flush=True)
print('\n')

@client.event
async def on_message(message):
    global start_count
    # temporary bypass to weird d.py cacheing issue
    # only print this info on the first time the client launches. this is due to d.py calling on_ready() after the bot regains connection
    if start_count == 0:
        if len(keywords) >= 1 and keywords[0] != '':
            print('+ Watching for keywords:  {}.\n'.format(', '.join(keywords)))
        else:
            print('+ No keywords have been provided.\n')
        if len(blacklist) > 0:
            print('+ Ignoring keywords    :  {}.\n'.format(', '.join(blacklist)))
        else:
            print('+ No keywords currently blacklisted.')
        print('+ {} is listening...\n'.format(str(client.user)))
        start_count += 1
    else:
        if message.channel.id in channels:
            if message.embeds:
                for embed in message.embeds:
                    toembed = embed.to_dict()
                    if str(toembed['type']).lower() != 'link':
                        urls = re.findall("(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'.,<>?«»“”‘’]))?",toembed['title'])
                        if urls:
                            await check_urls(urls)
                        try:
                            urls2 = re.findall("(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'.,<>?«»“”‘’]))?",toembed['description'])
                            if urls2:
                                await check_urls(urls2)
                        except:
                            pass
                        try:
                            for field in toembed['fields']:
                                urls3 = re.findall("(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'.,<>?«»“”‘’]))?",str(field))
                                if urls3:
                                    await check_urls(urls3)
                        except:
                            pass
            if message.content != '':
                # print_horizontal_line()
                print(f'\nURLs: \n{message.content}')
                # print_horizontal_line()
                urls4 = re.findall("(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'.,<>?«»“”‘’]))?",message.content)
                if urls4:
                    await check_urls(urls4)
            
keyboard.add_hotkey('q', lambda: client.loop.create_task(client.close()))

client.run(token)