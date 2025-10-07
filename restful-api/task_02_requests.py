import requests
import json
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for element in response.json():
            print(element['title'])


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them in posts.csv
    with columns: id, title, body
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        filtered_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_posts)
