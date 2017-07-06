#!/usr/bin/python

import sys

# Problem 17
# Write a program to write lines of a file in reverse order
# to another file
# also learning about command line
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def main(r, w):
    readFrom = open(r, 'r')
    lines = readFrom.readlines()[::-1]
    readFrom.close()

    writeTo = open(w, 'w')
    writeTo.writelines(lines)
    writeTo.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
