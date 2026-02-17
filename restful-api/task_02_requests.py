#!/usr/bin/python3
"""
Module that fetches and processes posts from JSONPlaceholder API
"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from the API and print the status code
    and titles of the posts.
    """
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts from the API and save selected fields
    (id, title, body) into a CSV file.
    """
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        formatted_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            writer.writeheader()
            writer.writerows(formatted_posts)
