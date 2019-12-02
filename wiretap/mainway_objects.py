from sqlalchemy.ext.declarative import declarative
from sqlalchemy.orm import column_property
from sqlalchemy import Column, Integer, String, ForeignKey
from wiretap.mainway_objects import *

Base = declarative_base()

class Poi(Base):
	__tablename__ = 'pois'
	id = Column(Integer, primary_key=True, autoincrement=True)
	discordid = Column(Integer)
	pos_comments = Column(Integer)
	neg_comments = Column(Integer)
	flagged_comments = Column(Integer)
	subversiveness = column_property(neg_comments / flagged_comments)
	locations = relationship('locations', secondary=location_poi, back_populates='pois')

class Locations(Base):
	__tablename__ = 'locations'
	id = Column(Integer, primary_key=True, autoincrement=True)
	type = Column(String, nullable=False)
	name = Column(String, nullable=False)
	pois = relationship('pois', secondary=location_poi, back_populates='locations')

class Incidents(Base):
	__tablename__ = 'incidents'
	id = Column(Integer, primary_key=True, autoincrement=True)
	writeup = Column(String)
	poi = Column(Integer, ForeignKey('pois.id'))
	location = Column(Integer, ForeignKey('locations.id'))