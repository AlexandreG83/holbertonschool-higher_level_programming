#!/usr/bin/python3
"""
List states matching a provided name from a MySQL database.

Usage:
    ./2-my_filter_states.py <user> <password> <database> <state_name>
"""

import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY states.id ASC;"
    ).format(state_name)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
