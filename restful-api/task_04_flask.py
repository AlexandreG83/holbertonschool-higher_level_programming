#!/usr/bin/python3
"""
Simple REST API built with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Point d'entrée racine
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Point d'entrée de statut
    """
    return "OK"


@app.route("/data")
def get_usernames():
    """
    Retourne la liste de tous les noms d'utilisateurs
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Retourne l'objet utilisateur complet par nom d'utilisateur
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur via une requête POST
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user
    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()
