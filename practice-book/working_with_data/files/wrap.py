#!/usr/bin/python

import sys

# Problem 21
# Take a filename and width as arguments
# and wrap lines longer than the width.

def main(filename, width):
    handle = open(filename, 'r')
    lines = handle.readlines()
    result = []
    for line in lines:
        i = len(line) // width + 1
        start = 0
        end = width
        while i > 0:
            result.append(line[start:end].strip())
            start = start + width
            end = end + width
            i = i - 1
    print '\n'.join(result)
    handle.close()

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

