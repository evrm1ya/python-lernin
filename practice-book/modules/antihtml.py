# Problem 6
# Write a program antihtml.py that takes a URL as argument,
# downloads the html from the web and prints it after
# string the html tags.

import sys
import re
import urllib

def main(url, path):
    response = urllib.urlopen(url)
    # text = response.read()
    # clean_text = re.sub('<.*?>', '', text)
    # handle = open(path, 'w')
    # handle.write(clean_text.strip())
    lines = response.readlines()
    handle = open(path, 'a')
    print lines
    for line in lines:
        cleaned = re.sub('<.*?>', '', line).strip()
        if cleaned == '':
            continue
        handle.write(cleaned + '\n')
    handle.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

