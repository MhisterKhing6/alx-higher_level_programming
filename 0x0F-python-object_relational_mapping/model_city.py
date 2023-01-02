#!/usr/bin/python3
"""Creates a base class that mapes a table"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
# Get declarative base object
engine = create_engine('mysql+mysqldb://:3036')
# get a declarative base object
Base = declarative_base()


class City(Base):
    """A class that maps table cities in the database"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
