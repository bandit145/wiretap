import wiretap.mainway_objects as mainway_objs


def create_item(session, item_type, **kwargs):
	item = getattr(mainway_objs, item_type)(**kwargs)
	session.add(item)
	session.commit()

def mainway_report(session, name, **kwargs):
	incidents = ''
	if 'id' in kwargs.keys():
		poi = session.query(mainway_objs.Poi).filter(mainway_objs.Poi.id == kwargs['id'])
	elif 'discordid' in kwargs['discordid']:
		poi = session.query(mainway_objs.Poi).filter(mainway_objs.Poi.discordid == kwargs['discordid'])
	reports = session.query(mainway_objs.Incidents.poi == poi.id).all()
	for incident in reports:
		incidents = '\t- {1} @type:{2} @location:{3}\n'.format(incident.writeup, )

	return '''```MAINWAY DATABASE REPORT:
	USER: {name}
	DISCORDID: {discordid}
	SUBVERSIVNESS: {subver}%
	INCIDENTS:
		- DID BAD THING
	END MAINWAY REPORT```'''.format(name=name, discordid=poi.discordid, subver=poi.subversiveness)