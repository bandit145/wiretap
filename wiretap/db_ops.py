import wiretap.mainway_objects as mainway_objs
import logging

async def create_item(session, item_type, **kwargs):
	item = getattr(mainway_objs, item_type)(**kwargs)
	session.add(item)
	session.commit()
	return item

async def get_item(session, item_type, **kwargs):
	pass

async def subversive_word(session, message):
	subver_word = session.query(mainway_objs.SubversiveWord).filter(mainway_objs.SubversiveWord.name_in_(message.lower()))
	if len(subver_word) > 0:
		return True
	return False

async def update_comments(session, poi, pos):
	poi.flagged_comments += 1
	if pos:
		poi.pos_comments += 1
	else:
		poi.neg_comments += 1
	session.commit()

async def mainway_report(session, name, **kwargs):
	incidents = ''
	if 'id' in kwargs.keys():
		poi = session.query(mainway_objs.Poi).filter(mainway_objs.Poi.id == kwargs['id'])[0]
	elif 'discordid' in kwargs.keys():
		poi = session.query(mainway_objs.Poi).filter(mainway_objs.Poi.discordid == kwargs['discordid'])[0]
	logging.info(poi)
	for incident in poi.incidents:
		location = session.query(mainway_objs.Location).filter(mainway_objs.Location.id == incident.location)[0]
		incidents += '\t\t- {0} @type:{1} @location:{2} @date:{3}\n'.format(incident.writeup, 
			incident.type, location.name, incident.date)

	return '''```MAINWAY DATABASE REPORT:
	USER: {name}
	DISCORDID: {discordid}
	SUBVERSIVNESS: {subver}%
	INCIDENTS:
{incidents}
	END MAINWAY REPORT```'''.format(name=name, discordid=poi.discordid, subver=poi.subversiveness, incidents=incidents)