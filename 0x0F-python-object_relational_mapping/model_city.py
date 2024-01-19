#!/usr/bin/python3
"""
class definition for city
"""


from sqlalchemy import ForeignKey, Column, Integer, String
import MySQLdb
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    inherits from Base, cities table object
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", backref="children")
