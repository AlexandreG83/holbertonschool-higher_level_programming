#!/usr/bin/python3
"""
List states matching a provided name from a MySQL database.

This script uses a parameterized query to prevent SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        charset="utf8"
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY states.id ASC"
    )
    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
