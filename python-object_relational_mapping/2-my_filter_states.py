#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and filters by user input."""
    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database, charset="utf8")

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
