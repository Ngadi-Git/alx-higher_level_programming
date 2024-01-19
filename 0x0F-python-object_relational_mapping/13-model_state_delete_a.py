#!/usr/bin/python3
"""
script to delete objects with name containing a
"""


from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    names_a = State.__table__.\
        delete().\
        where(State.name.like(func.binary('%a%')))
    session.execute(names_a)
    session.commit()

    session.close()
