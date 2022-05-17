import requests
import json
import time

rate_limit_prevent = time.sleep(0.1)


def data_requester(new_posts):
    # Authors set
    authors = set()
    # Request post
    for post_id in new_posts:
        rate_limit_prevent
        post = requests.get("https://hacker-news.firebaseio.com/v0/item/"+ str(post_id) + ".json")
        post_content_to_dump = []

        # Check request is not 404
        if post.ok:
            post = post.json()

            # Write data to file
            with open("data/post_" + str(post_id) + ".txt","w",encoding="utf-8") as post_file:
                # Recursively write to post_content_to_dump
                recursive_post_requester(post, post_content_to_dump, authors)
                # Dump array to file
                json.dump(post_content_to_dump,post_file,sort_keys=True, indent=4)

            post_file.close()

        else:
            print("Post request failed")

    return authors


def recursive_post_requester(post, post_content_to_dump, authors):

    # Add author to list
    if "by" in post:
        authors.add(post["by"])

    # Append to content to dump
    post_content_to_dump.append(post)

    # Request from each kid if they exist
    if "kids" in post:
        for post_comment_id in post["kids"]:
            rate_limit_prevent
            post_comment = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(post_comment_id) + ".json").json()
            recursive_post_requester(post_comment, post_content_to_dump, authors)
