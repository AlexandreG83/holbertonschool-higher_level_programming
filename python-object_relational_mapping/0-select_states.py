#!/usr/bin/python3
"""
Liste tous les états depuis une base de données MySQL.

Usage:
    ./0-select_states.py <user> <password> <database>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Récupère les arguments de la ligne de commande
    user = sys.argv[1]
    passeword = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passeword,
        db=db_name
    )

    # Exécution de la requête et affichage des résultats
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
