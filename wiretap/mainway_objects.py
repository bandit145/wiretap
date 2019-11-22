from sqlalchemy.ext.declarative import declarative
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Poi(Base):
	__tablename__ = 'pois'
	id = Column(Integer, primary_key=True)