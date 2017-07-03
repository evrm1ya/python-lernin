# Problem 7
# Write a program `links.py` that takes a URL as an argument
# and prints all the URLs linked from that webpage.

# TODO
# Can expand on this to filter out scripts, stylesheets, external links, etc

import sys
import re
import urllib
import json

def main(url, filename):
    response = urllib.urlopen(url)
    text = response.read()
    handle = open(filename, 'w')
    links = re.findall(r'href=\"(.*?)\"', text)
    handle.write(json.dumps(links, indent=2))
    handle.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
