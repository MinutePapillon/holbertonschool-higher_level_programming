#!/usr/bin/python3
"""
Lists all states with names starting with 'N' from hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and filters states starting with N."""
    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
