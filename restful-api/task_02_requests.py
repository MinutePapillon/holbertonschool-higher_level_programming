import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: ", response.status_code)
    data = response.json()

    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    with open('posts.csv', 'w', newline='', encoding="utf-8") as fichier:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(fichier, fieldnames=fieldnames)
        writer.writeheader()

        for post in data:
            writer.writerow({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]})
