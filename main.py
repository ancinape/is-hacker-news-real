import requests
import os
from src.dataformatting import data_requester
from src.fileintostrings import read_files_into_strings

# Remove previous data
#os.remove("./data/*")

# Latest 500 stories
new_posts = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json").json()

authors = data_requester(new_posts)
#string = read_files_into_strings()
#print(string)