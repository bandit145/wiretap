from elasticsearch_async import AsyncElasticsearch
from ssl import create_default_context

def elasticsearch_session(url, config):
	ssl_context = None
	http_auth = None
	if 'elastic_user' in config['main'].keys():
		http_auth = (config['main']['elastic_user'], config['main']['elastic_password'])
	if 'ssl_verify' in config['main'].keys():
		if 'ca_file' in config['main'].keys():
			ca_file = config['main']['ca_file']
		else:
			ca_file = '/etc/pki/etc/ca'
		ssl_context = create_default_context(cafile=ca_file)
	return AsyncElasticsearch(url, ssl_context=ssl_context, http_auth=http_auth)

async def create_new_server_index(es, guild_id):
	if not await es.indices.exists(index='wiretap_discord_{0}_1'.format(guild_id)):
		await es.indices.create(index='wiretap_discord_{0}_1'.format(guild_id))
	await es.indices.put_alias(index='wiretap_discord_{0}*'.format(guild_id), name='wiretap_discord_{0}'.format(guild_id))

async def get_active_index(es, guild_id):
	indices = await es.indices.get(index='wiretap_discord_{0}*'.format(guild_id))
	index_list = list(indices.keys())
	return index_list[len(index_list)-1]

async def store_message(es, message, guild_id):
	index_name = await get_active_index(es, guild_id)
	await es.index(index=index_name, doc_type='discord_message', body=message)



# async def create_server_index(es, guild):
# 	indices = es.indices.get(index='wiretap_discord_{0}*'.format(guild.id))
# 	if len(indices) == 0:
# 		es.indices.create(index='wiretap_discord_{0}_1'.format(guild.id))
# 	else:
# 		indice_num = int(indices[0]['_index'].split('_')[2])
# 		es.indices.create(index='wiretap_discord_{0}_1'.format(guild.id))
# 	es.indices.put_alias(index='wiretap_discord_{0}*'.format(guild.id), name='wiretap_discord_{0}'.format(guild.id))

