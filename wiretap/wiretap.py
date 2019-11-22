import discord
import logging
import os
from bot_funcs import client

def get_config():
	config = {}
	config['token'] = os.getenv('wiretap_token')
	return config

def configure_logging():
	logging.basicConfig(level=logging.INFO)

configure_logging()
config = get_config()
client.run(config['token'])