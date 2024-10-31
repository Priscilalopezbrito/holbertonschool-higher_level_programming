#!/usr/bin/python3

"""
Cities in state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
