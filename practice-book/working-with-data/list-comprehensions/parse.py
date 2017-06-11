# Problem 30 and 21
# Write a function `parse` to
# parse files based on any delimiter
# and filter out commented lines.

import sys

def parse(lines, delimiter, comment):
    return [line.strip().split(delimiter) for line in lines if line[0] != comment]

def main(f, delimiter, comment):
    handle = open(f, 'r')
    lines = handle.readlines()
    handle.close()
    print parse(lines, delimiter, comment)

# python parse.py commas.csv "," "#"
# TODO: look at better argument passing
if __name__ == '__main__':
    args = sys.argv
    print args
    main(args[1], args[2], args[3])

