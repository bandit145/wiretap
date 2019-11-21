import discord
import logging
import os

client = discord.Client()
def get_config():
	config = {}
	config['token'] = os.getenv('wiretap_token')
	return config

def configure_logging():
	pass


@client.event
async def on_ready():
	print('wiretap enabled')

@client.event
async def on_guild_join(guild):
	for chan in guild.text_channels:
		await chan.send('**click**')


@client.event
async def on_message(message):
	if client.user in message.mentions:
		await message.channel.send('**click**')
	elif client.user == message.author:
		await message.delete(delay=3)


config = get_config()
client.run(config['token'])