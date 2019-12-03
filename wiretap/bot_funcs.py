import discord
import os
import logging
from textblob import TextBlob
import wiretap.db_ops as db_ops
import wiretape.elasticsearch as elasticsearch
import re

# utility functions

async def analyse_message(client, message):
	if await db_ops.subversive_word(client.db, message.content):
		await message.add_reaction('🟥')
		poi = await db_ops.get_item(client.db, 'Poi', discordid=message.author.id)
		sentiment = await message_sentiment(client.config, message.content)
		if sentiment:
			await db_ops.update_comments(client.db, poi, sentiment)
		else:
			await db_ops.update_comments(client.db, poi, sentiment)
		return True
	else:
		return False

async def index_message(client, message):

async def wiretap_mentioned(client, message):
	if client.user in message.mentions:
		await message.channel.send('**click**')
		await message.delete(delay=3)
		return True
	return False

async def mainway_report(message):
	if re.match('\$report:',message.content.lower()):
		report = await db_ops.mainway_report(message.mentions[0].name, discordid=message.mentions[0].id)
		await message.channel.send(report)
		return True
	return False

async def message_sentiment(config, message):
	msg_blob = TextBlob(message)
	if msg_blob.sentiment[0] >  float(config['main']['subver_cutoff']):
		return True
	return False

# bot reaction functions

@client.event
async def on_ready(self):
	logging.info('wiretap online')

@client.event
async def on_guild_join(self, guild):
	await elasticsearch.create_server_index(client.es, guild)
	for chan in guild.text_channels:
		message = await chan.send('**click**')
		await message.delete(delay=3)

@client.event
async def on_message(self, message):
	await index_message(client, message)
	if await analyse_message(client, message):
		return
	if await wiretap_mentioned(client, message):
		return
	if await mainway_report(message):
		return