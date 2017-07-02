#!/usr/bin/python
import sys
import os

# Problem 4
# Write a program to print a directory tree.
# The program should take the path of a directory
# as an argument and print all the files in it
# recurively as a tree.

def is_not_dot_dir(fname):
    return fname[0] != '.'
    
def dirtree(path, indents):
    files = os.listdir(path)
    indent = '|    ' * indents
    for f in files:
        print indent + '|-- ' + f
        fullpath = path + '/' + f
        if os.path.isdir(fullpath) and is_not_dot_dir(f):
            dirtree(fullpath, indents + 1)
    
if __name__ == '__main__':
    dirname = sys.argv[1]
    print dirname
    dirtree(dirname, 0)

