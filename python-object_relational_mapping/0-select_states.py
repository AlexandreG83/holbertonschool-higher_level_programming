#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
Connects to a MySQL database using MySQLdb and prints all rows
from the states table ordered by id.
"""

import MySQLdb
import sys


def list_states():
    """
    Connects to the MySQL database and prints all states
    ordered by states.id in ascending order.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
