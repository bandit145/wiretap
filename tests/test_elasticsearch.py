import wiretap.elasticsearch as wiretap_es
from elasticsearch import Elasticsearch
import asyncio
import logging

ELK_HOST = 'localhost:9200'

def es_init():
	return Elasticsearch(ELK_HOST)

async def real_es_init():
	return wiretap_es.elasticsearch_session(ELK_HOST, {'main':{}})

# def test_elasticsearch_session():
# 	es = wiretap_es.elasticsearch_session(ELK_HOST, {'main':{}})
# 	assert not es.indices.exists(index='testthing')

def test_create_new_index():
	test_es = es_init()
	es = asyncio.get_event_loop().run_until_complete(real_es_init())
	asyncio.get_event_loop().run_until_complete(wiretap_es.create_new_server_index(es, 1))
	logging.info('Starting index: {}'.format(test_es.indices.get(index='wiretap_discord_1_1')))
	assert es.indices.exists(index='wiretap_discord_1_1')

def test_index():
	message = {
		'author': 100057952664162304,
		'msg_id': 100057952664162305,
		'content': 'random message hurdurr @dan @wat @test',
		'channel': {'id':2, 'name': 'mychan'},
		'mentions': [100057952664162306, 100057952664162307, 100057952664162308]

	}
	test_es = es_init()
	es = asyncio.get_event_loop().run_until_complete(real_es_init())
	asyncio.get_event_loop().run_until_complete(wiretap_es.store_message(es, message, 1))
	es.indices.refresh(index='wiretap_discord_1_1')
	data = test_es.search(index='wiretap_discord_1_1', body={'query':{'match_all':{}}})
	logging.info('message data {}'.format(data))

# def test_some_index_shit():
# 	es = es_init()
# 	# es.indices.create(index='testthing1')
# 	# es.indices.create(index='testthing2')
# 	indices = es.indices.get(index='testthing*')
# 	logging.info(indices.keys())
# 	#logging.info(es.indices.get(index='testthing*'))
