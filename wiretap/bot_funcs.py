import discord
import os
import logging
from textblob import TextBlob
import re

# utility functions
	 
def is_subversive_word(message):
	if 'communist' in message:
		return True
	return False

# bot functions

class Wiretap(discord.Client):
	@client.event
	async def on_ready(self):
		logging.info('wiretap online')

	@client.event
	async def on_guild_join(self, guild):
		for chan in guild.text_channels:
			message = await chan.send('**click**')
			await message.delete(delay=3)


	@client.event
	async def on_message(self, message):
		print(config)
		if is_subversive_word(message):
			await message.add_reaction('🟥')

		if client.user in message.mentions:
			await message.channel.send('**click**')
			await message.delete(delay=3)
		elif re.match('\$report:',message.content.lower()):
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