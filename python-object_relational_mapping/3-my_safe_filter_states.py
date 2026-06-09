#!/usr/bin/python3
"""
Displays all values in states where name matches the argument
Safe from SQL injection
Usage: ./3-my_safe_filter_states.py <username> <password>
    <database> <state_name>
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
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY states.id ASC"
    )
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
