from sqlalchemy import create_engine
import asyncio
from sqlalchemy.orm import sessionmaker
import wiretap.mainway_objects as objs
import wiretap.db_ops as db_ops
import datetime
import logging

def define_db():
	engine = create_engine('sqlite:///wiretap_test.sqlite')
	objs.Base.metadata.create_all(engine)
	return sessionmaker(bind=engine)()

def clear_table(session, name):
	session.execute('delete from {}'.format(name))
	session.commit()

def test_poi_create():
	discordid = 100057952664162304
	session = define_db()
	asyncio.get_event_loop().run_until_complete(db_ops.create_item(session, 'Poi', discordid=discordid))
	data = session.execute('select * from pois where discordid=:discordid',{'discordid': discordid}).fetchall()
	assert data[0][1] == discordid
	logging.info(data[0])
	clear_table(session, 'pois')

def test_mainway_report():
	discordid = 100057952664162304
	session = define_db()
	poi = asyncio.get_event_loop().run_until_complete(db_ops.create_item(session, 'Poi', discordid=discordid, pos_comments=100, neg_comments=50, flagged_comments=150))
	location = asyncio.get_event_loop().run_until_complete(db_ops.create_item(session, 'Location', type='discord', name='test server', pois=[poi]))
	asyncio.get_event_loop().run_until_complete(db_ops.create_item(session, 'Incident', writeup='bad thing', type='kick', poi=poi.id, location=location.id, date=datetime.datetime.now()))
	asyncio.get_event_loop().run_until_complete(db_ops.create_item(session, 'Incident', writeup='bad thing2', type='kick', poi=poi.id, location=location.id, date=datetime.datetime.now()))
	report  = asyncio.get_event_loop().run_until_complete(db_ops.mainway_report(session, 'bad user', discordid=discordid))
	logging.info(report)
	assert type(report) == str

		