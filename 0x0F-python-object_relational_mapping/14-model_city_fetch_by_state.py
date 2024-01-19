#!/usr/bin/python3
"""
script to list all city objects
"""


from sys import argv
from model_state import Base, State
from model_city import Base, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City, State).\
            join(State).\
            order_by(City.id).all():
        print("{}: ({}) {}".format(
                city.State.name,
                city.City.id,
                city.City.name))

    session.close()
