#!/usr/bin/python3
"""
Lists all states with a name starting with N (uppercase N)
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Création du curseur
    cur = db.cursor()

    # Exécution de la requête SQL
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture des connexions
    cur.close()
    db.close()
