x = set([3, 1, 2, 1])

print set(x)
print {3, 1, 2, 1}

x.add(4)
print x

print 1 in x
print 5 in x

# Problem 15
# Another `unique` implementation

def unique(values, fn=None):
    if fn != None:
        return set([fn(x) for x in values]) 
    return set(values)

print unique([9, 2, 2, 5, 3, 5, 1, 9])
print unique(['python', 'java', 'Java', 'Python'], fn=lambda s: s.upper())

