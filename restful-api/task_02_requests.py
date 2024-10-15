#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
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
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        struct_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(struct_data)
    else:
        print("Failed to fetch posts")
