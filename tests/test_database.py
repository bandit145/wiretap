from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wiretap.mainway_objects import *

def define_db():
	engine = create_engine('sqlite:///:memory:')
	return sessionmaker(bind=engine)

def test_poi_ops():
	engine = define_db()
		