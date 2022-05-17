import requests
import os
from dataformatting import data_requester
from fileintostrings import read_files_into_strings

# Remove previous data
#os.remove("./data/*")

# Latest 500 stories
new_posts = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json").json()

string = read_files_into_strings()
#data_requester(new_posts)