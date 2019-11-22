import discord
import logging
import os
from wiretap.bot_funcs import client
from wiretap.mainway_schema import metadata
from sqlalchemy import create_engine
import configparser

def get_config(config_file):
	config = configparser.ConfigParser()
	config.read(config_file)
	return config

def configure_logging():
	logging.basicConfig(level=logging.INFO)

async def start_bot(**kwargs):
	configure_logging()
	if 'config' in kwargs.keys():
		conf_path = kwargs['config']
	else:
		conf_path = 'wiretap.conf'
	config = get_config(conf_path)
	engine = create_engine(config['main']['db_string'])
	metadata.create_all(engine)
	client.run(config['main']['token'])