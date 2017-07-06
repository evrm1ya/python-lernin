#!/usr/bin/python

import sys

# Problem 20
# Implement `grep` to print lines that have the specified string

def main(filename, string):
    handle = open(filename, 'r')
    lines = handle.readlines()
    print ''.join([x for x in lines if string in x])
    handle.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

