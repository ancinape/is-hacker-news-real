import json
from glob import glob
# A function that compiles all of the text files associated with a single author into a single string
def read_files_into_strings(filepath="./data/post_*.txt"):
    strings = []
    filenames = glob(filepath)
    for filename in filenames:
        with open(filename) as post_file:
            posts = json.load(post_file)
            #TODO Get only title and/or text of posts in each post file.
            for post in posts:
                strings.append(post["title"])
                if "text" in post:
                    strings.append(post["text"])
    return '\n'.join(strings)