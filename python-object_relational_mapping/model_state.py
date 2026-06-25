#!/usr/bin/python3
"""Définit la classe State et la base déclarative"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Création de la base déclarative SQLAlchemy
Base = declarative_base()


class State(Base):
    """Classe State qui fait le lien avec la table states"""

    # Nom de la table dans la base de données
    __tablename__ = "states"

    # Colonnes de la table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
