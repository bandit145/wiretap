import discord
import os
import logging
from textblob import TextBlob
import re
client = discord.Client()

# utility functions
async def subversive_word(message):
	if is_subversive_word(message.content):
		await message.add_reaction('🟥')
	 
def is_subversive_word(message):
	if 'communist' in message:
		return True
	return False

# bot functions
@client.event
async def on_ready():
	logging.info('wiretap online')

@client.event
async def on_guild_join(guild):
	for chan in guild.text_channels:
		await chan.send('**click**')


@client.event
async def on_message(message):
	await subversive_word(message)
	if client.user in message.mentions:
		await message.channel.send('**click**')
	elif re.match('\$REPORT:',message.content):
		name = message.content.split(':')[1]
		await message.channel.send('''
			```MAINWAY DATABASE REPORT:
USER: {name}
DISCORDID: TEST
SUBVERSIVNESS: 100%
INCIDENTS:
	- DID BAD THING
END MAINWAY REPORT```
		'''.format(name=name))
	elif client.user == message.author:
		await message.delete(delay=3)