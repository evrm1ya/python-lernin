#!/usr/bin/python

# Problem 34
# Improve word_frequency to print the words 
# in the descending order of the number of occurrences.

def word_frequency_descending(frequency):
    """Returns a list of words sorted in descending order
        based on frequency.
        
        print frequency_descending({'a': 1, 'b': 3, 'c': 2})
        ['b', 'c', 'a']
    """
    return sorted(frequency, key=frequency.get, reverse=True)

def word_frequency(words):
    """Returns frequency of each word given in a list of words.
       
       print word_frequency(['a', 'b', 'a'])
       {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

# print word_frequency(['py', 'js', 'js', 'py', 'clj'])

def read_words(filename):
    return open(filename).read().split()

def main(filename):
    words = read_words(filename)
    frequency = word_frequency(words)
    print frequency
    print word_frequency_descending(frequency)
    for word, count in frequency.items():
        print word, count

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
