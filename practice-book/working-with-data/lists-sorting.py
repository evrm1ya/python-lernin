# `sort` mutates
# `sorted` returns a new sorted list

# Problem 13
# Write a function `lensort` to sort a list of
# strings based on length

def lensort(strings):
    return sorted(strings, key=lambda s: len(s))

print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])

# Problem 14
# Improve `unique` by taking an optional key
# function as argument and use the return value of the
# key function to check for uniqueness.

def unique(values, fn=lambda x: x):
    cache = {}
    result = []
    for x in values:
        key = fn(x)
        if key in cache:
            continue
        cache[key] = 1
        result.append(key)
    return result

print unique([1, 2, 1, 3, 2, 5])
print unique(['python', 'java', 'Python', 'Java'], fn=lambda s: s.lower())

collection = [ 
        { 'a': 1, 'b': 2 },
        { 'a': 4, 'b': 3 },
        { 'a': 1, 'b': 4 },
        { 'a': 2, 'b': 5 },
        { 'a': 2, 'b': 6 },
        { 'a': 1, 'b': 6 },
        { 'a': 3, 'b': 6 } ]

assert unique(collection, fn=lambda x: x['a']) == [1, 4, 2, 3]
