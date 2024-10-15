#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    #  Print the status code of the response
    print("Status Code: {}".format(response.status_code))

    #  If successful, parse the fetched data into a JSON object
    if response.status_code == 200:
        posts = response.json()
        #  Iterate through JSON data and print the titles of all posts
        for post in posts:
            print(post["title"])

    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["userId", "id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
    else:
        print("Failed to fetch posts")
