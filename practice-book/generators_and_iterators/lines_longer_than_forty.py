# Problem 2
# Write a program that takes one or more filenames
# as arguments and prints all the lines which are longer than 40 characters.

# could use this to test for character recommendations in code standards

import sys

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            length = len(line)
            yield (f, length, line)

def longer_than_forty_chars(lines):
    return ((f, length, line) for (f, length, line) in lines if len(line) > 40)

def printlines(lines):
    for line in lines:
        f, length, line = line
        print f, '(' + str(length) + '):', line

def main(filenames):
    lines = readfiles(filenames)
    lines = longer_than_forty_chars(lines)
    printlines(lines)

if __name__ == '__main__':
    main(sys.argv[1:])

# python lines_longer_than_forty.py ./files/*.txt
