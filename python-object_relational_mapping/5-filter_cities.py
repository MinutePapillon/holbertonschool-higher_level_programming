#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and lists cities by given state name."""
    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database, charset="utf8")

    cur = db.cursor()
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))
    cities = [city[0] for city in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
