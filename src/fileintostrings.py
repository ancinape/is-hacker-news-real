import json
from glob import glob
from bs4 import BeautifulSoup

# A function that compiles all of the text files associated with a single author into a single string
def read_files_into_strings(filepath="./data/post_*"):
    strings = []
    filenames = glob(filepath)
    for filename in filenames:
        with open(filename,"r",encoding="utf-8") as post_file:
            posts = json.load(post_file)
            #TODO Get only title and/or text of posts in each post file.
            for post in posts:
                if "title" in post:
                    strings.append(strip_html(post["title"]))
                if "text" in post:
                    strings.append(strip_html(post["text"]))
        post_file.close()
    return '\n'.join(strings)

def strip_html(string):
    string_soup = BeautifulSoup(string, "html.parser")

    # Extra modifications to string would go here

    string_stripped = string_soup.get_text()
    return string_stripped