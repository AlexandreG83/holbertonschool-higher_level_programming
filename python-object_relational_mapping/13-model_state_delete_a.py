#!/usr/bin/python3
"""
Deletes all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """
    Connects to the MySQL database and deletes all states
    whose name contains the letter 'a'.
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            user, password, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
