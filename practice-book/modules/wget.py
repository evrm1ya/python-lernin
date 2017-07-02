#!/usr/bin/python
# Problem 5
# Write a program wget.py to download a given URL.
# The program should accept a URL as argument,
# download it and save it with the basename of
# the URL. If the URL ends with a /, consider the
# basename as index.html.

import sys
import urllib

def main(url, filename):
    response = urllib.urlopen(url)
    handle = open(filename, 'w')
    handle.write(response.read())
    handle.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

