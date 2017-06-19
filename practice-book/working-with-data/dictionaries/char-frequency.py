#!/usr/bin/python

# Problem 34
# Write a program to count frequency of characters
# in a given file. Can you use character frequency
# to tell whether the given file is a Python 
# program file, JS program file, or a text file?

def character_frequency(text):
    """Returns the frequency of characters in the text.
    """
    frequency = {}
    for c in text:
        frequency.setdefault(c, 0)
        frequency[c] = frequency[c] + 1
    return frequency

# python shouldn't have '{', '}' 
# JS probably won't have '#'
# txt file probably won't have '[' or ']'
def main(filename):
    text = open(filename).read()
    frequency = character_frequency(text)
    print frequency

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
