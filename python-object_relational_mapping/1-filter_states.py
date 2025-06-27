#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", ("N%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
