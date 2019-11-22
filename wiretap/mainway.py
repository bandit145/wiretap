from sqlalchemy import MetaData, Table, Column, String, ForeignKey

metadata = MetaData()

#persons of interest table
pois = Table('pois', metadata,
	Column('id', Integer, primary_key=True),
	Column('discordid', Integer),
	Column('pos_comments', Integer),
	Column('neg_comments', Integer)
	)

location_poi = Table('location_po', metadata,
	Column('location', None, ForeignKey('locations.id')),
	Column('poi', None, ForeignKey('pois.id'))
	)

locations = Table('locations', metadata,
	Column('id', Integer, primary_key=True),
	Column('type', String, nullable=False),
	Column('name', String, nullable=False)
	)

incidents = Table('incidents', metadata,
	Column('id', Integer, primary_key=True),
	Column('writeup', String),
	Column('poi', None, ForeignKey('poi.id'))
	)

location_incident = Table('location_incident', metadata,
	Column('location', None, ForeignKey('locations.id')),
	Column('incident', None, ForeignKey('incident.id'))
	)