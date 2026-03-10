#!/usr/bin/python3
"""
Module that prints the first State object from the database hbtn_0e_6_usa.
Uses SQLAlchemy ORM to query the states table and display the state
with the smallest id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state():
    """
    Connects to the MySQL database and prints the first State
    ordered by states.id. Prints 'Nothing' if no state exists.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    fetch_first_state()
