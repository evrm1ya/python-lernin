#!/usr/bin/python

import sys

# Problem 18
# Write a program to print each line of a file in reverse order

def main(f):
    handle = open(f, 'r')
    print ' '.join([x[::-1] for x in handle.readlines()])
    handle.close()

if __name__ == '__main__':
    main(sys.argv[1])
