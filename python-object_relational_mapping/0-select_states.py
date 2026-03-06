#!/usr/bin/python3
"""
List all states from a MySQL database.

Usage:
    ./0-select_states.py <user> <password> <database>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    "Retrive command argument"
    user = sys.argv[1]
    passeword = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passeword,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
