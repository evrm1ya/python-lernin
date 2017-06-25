#!/usr/bin/python
import sys
import os

# Problem 2
# Write a program `extcount.py` to count the number of files
# for each extension in the given directory. The program
# should take a directory name as argument and print
# the count and extension for each available file extension.

def main(path):
    frequency = {}
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        frequency[ext] = frequency.get(ext, 0) + 1
    for k, v in frequency.items():
        print k, v

if __name__ == '__main__':
    main(sys.argv[1])

