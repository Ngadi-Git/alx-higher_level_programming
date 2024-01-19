#!/usr/bin/python3
"""
class definition for state
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import MySQLdb


Base = declarative_base()


class State(Base):
    """
    inherits from Base, states table object
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """
        init with name
        """
        self.name = name
