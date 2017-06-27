#!/usr/bin/python
import sys
import os
import time

# Problem 3
# Write a program to list all the files in the given
# directory along with their length and last modification
# time. The output should contain one line for each file
# containing filename, length and modification date 
# separated by tabs.

def main(path):
    print 'filename\tbytes\tlast_modified'
    for f in os.listdir(path):
        stats = os.stat(path + '/' + f)
        print f + '\t' + str(stats.st_size) + '\t' + time.ctime(stats.st_mtime)

if __name__ == '__main__':
    main(sys.argv[1])

