#!/usr/bin/python3
"""
Module that prints the id of the State object
whose name is passed as argument.
Uses SQLAlchemy ORM to interact with the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name():
    """
    Connects to the MySQL database and prints the id
    of the state matching the name provided as argument.
    If no state is found, prints 'Not found'.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    get_state_by_name()
