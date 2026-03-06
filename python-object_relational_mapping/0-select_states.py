#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
using MySQLdb module. Results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création du curseur et exécution de la requête
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
