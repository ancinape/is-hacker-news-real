import requests
import json
import time

rate_limit_prevent = time.sleep(0.1)


def data_requester(new_posts):
    # Request post
    for post_id in new_posts:
        rate_limit_prevent
        post = requests.get("https://hacker-news.firebaseio.com/v0/item/"+ str(post_id) + ".json")

        # Check request is not 404
        if post.ok:
            post = post.json()

            # Write data to file
            with open("data/post_" + str(post_id) + ".txt","w",encoding="utf-8") as post_file:
                # Recursively write comments
                recursive_post_requester(post, post_file)
            post_file.close()

        else:
            print("Post request failed")


def recursive_post_requester(post, post_file):
    rate_limit_prevent

    # Dump post
    json.dump(post, post_file, sort_keys=True, indent=4)

    # Request from each kid if they exist
    if "kids" in post:
        for post_comment_id in post["kids"]:
            post_comment = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(post_comment_id) + ".json").json()
            recursive_post_requester(post_comment, post_file)
