#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
It connects to a MySQL server using MySQLdb and retrieves all
records from the table 'states', sorted by id in ascending order.
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists all states ordered by id in ascending order.
    """
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor and execute the query
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
