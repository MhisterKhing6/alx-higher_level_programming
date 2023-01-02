#!/bin/usr/python3
"""Creates a base class that mapes a table"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
# Get declarative base object
Base = declarative_base()
engine = create_engine('mysql+mysqldb://:3036')


class State(Base):
    """A class that maps table state in the database"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
