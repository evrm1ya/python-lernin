#!/usr/bin/python
import sys
import os

# Problem 1
# Write a program to list all files in the given directory.
if __name__ == '__main__':
    for f in os.listdir(sys.argv[1]):
        print f

