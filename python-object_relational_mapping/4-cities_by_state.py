#!/usr/bin/python3
"""
Liste toutes les villes avec leur nom d'état correspondant.
Utilisation : ./4-cities_by_state.py <utilisateur> <mot_de_passe> <base_de_données>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Exécution de la requête avec jointure entre cities et states
    cur = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )
    cur.execute(query)

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
