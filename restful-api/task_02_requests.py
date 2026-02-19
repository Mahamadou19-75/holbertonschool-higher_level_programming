import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints:
    - the status code
    - the title of each post if the request is successful
    """
    response = requests.get(API_URL)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse and print titles
    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post.get("title"))
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetches posts and saves them into a CSV file (posts.csv)
    containing the fields: id, title, body
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        # Prepare data as a list of dictionaries
        filtered_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in data
        ]

        # Write the CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)

        print("posts.csv saved successfully.")
    else:
        print("Error: Could not fetch posts.")
