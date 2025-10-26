#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument safely.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and safely filters by user input."""
    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
