#!/usr/bin/python3
"""Module de sérialisation de base :
Sérialise un dictionnaire Python en fichier JSON
Désérialise un fichier JSON en dictionnaire Python
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.

    Args:
        data (dict): Dictionnaire Python à sérialiser.
        filename (str): Nom du fichier JSON de sortie.
    """
    # Ouverture du fichier en écriture avec encodage UTF-8
    with open(filename, 'w', encoding='utf-8') as f:
        # Conversion du dictionnaire en JSON et écriture dans le fichier
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge et désérialise un fichier JSON en dictionnaire Python.

    Args:
        filename (str): Nom du fichier JSON d'entrée.

        Returns:
        dict: Dictionnaire Python désérialisé depuis le fichier JSON.
    """
    # Ouverture du fichier en lecture avec encodage UTF-8
    with open(filename, 'r', encoding='utf-8') as f:
        # Lecture et conversion du JSON en dictionnaire Python
        return json.load(f)
