# TODO: anagrams could use a second look
# Problem 36
# Write a program to find anagrams in a given list
# of words. Two words are called anagrams if one word
# can be formed by rearranging letters of another.
# ex.) 'eat', 'ate', and 'tea' are anagrams

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']

def character_frequency(word):
    frequency = {}
    for c in word:
        frequency.setdefault(c, 0)
        frequency[c] = frequency[c] + 1
    return frequency

def character_frequencies_are_equal(freq_a, freq_b):
    for k,v in freq_a.items():
        if not k in freq_b:
            return False
        if v != freq_b[k]:
            return False
    return True

def anagrams(words):
    result = []
    words_used = {}
    length = len(words)
    for i,w in enumerate(words):
        if w in words_used:
            print 'used:', w
            continue
        words_used[w] = 1
        local = [w]
        freq = character_frequency(w)
        for word_b in words[i + 1:length]:
            if character_frequencies_are_equal(freq, character_frequency(word_b)):
                local.append(word_b)
                words_used[word_b] = 1
        result.append(local)
    return result

print anagrams(words)

# Problem 37
# Write a function `valuesort` to sort values of a 
# dictionary based on the key.

def valuesort(dictionary):
    sorted_keys = sorted(dictionary)
    return [dictionary.get(key) for key in sorted_keys]

print valuesort({'x': 1, 'y': 2, 'a': 3})

# Problem 38
# Write a function `invertdict` to interchange keys
# and values in a dictionary. For simplicity, assume
# that all values are unique.

def invertdict(dictionary):
    new_dict = {}
    for k,v in dictionary.items():
        new_dict[v] = k
    return new_dict

print invertdict({'x': 1, 'y': 2, 'z': 3})
