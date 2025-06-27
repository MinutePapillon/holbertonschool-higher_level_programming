#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création du curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Exécution de la requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture de la connexion
    cursor.close()
    db.close()
