# Problem 24
# Provide an implementation for `zip`
# using list comprehensions

def new_zip(list1, list2):
    if len(list1) <= len(list2):
        return [(x, list2[i]) for i,x in enumerate(list1)]
    return [(list1[i], y) for i,y in enumerate(list2)]
 
print new_zip([1, 2, 3], ['a', 'b', 'c'])
print new_zip([1, 2, 3], ['a', 'b', 'c', 'd'])
print new_zip([1, 2, 3, 4], ['a', 'b', 'c'])

# Problem 25
# Provide an implementation for `map`
# using list comprehensions.

def square(x): return x * x

def new_map(fn, items):
    return [fn(x) for x in items]

print new_map(square, range(5))

# Problem 26
# Provide an implementation for `filter`
# using list comprehensions

def even(x): return x % 2 == 0

def isGreaterThan(y):
    def f(x):
        return x > y
    return f

def new_filter(fn, items):
    return [x for x in items if fn(x)]

print new_filter(even, range(10))
print new_filter(isGreaterThan(5), range(10))

# Problem 27
# Write a function `triplets` that takes a number `n`
# as argument and returns a list of triplets such that
# the sum of the first two elements of the triplet equals
# the third element using numbers below `n`.
# Note that (a, b, c) and (b, a, c) represent the same triplet.

def triplets(number):
    r = range(1, number) 
    return [(x, y, z) for x in r for y in r for z in r if x <= y and x + y == z]

print triplets(5)

# Problem 28
# Write a function `enumerate` that takes a list and 
# returns a list of tuples containing `(index, item)`
# for each item in the list.

def new_enumerate(items):
    return [(i, items[i]) for i in range(0, len(items))] 

enum_items = ['a', 'b', 'c']
enumerated = new_enumerate(enum_items)
print enumerated
enum_items[2] = 'd'
print enum_items
print enumerated

# Problem 29
# Write a function `array` to create a 
# 2D array. Both dimensions should be passed
# as arguments. Values can be initialized to None.

def two_d_array(x, y):
    return [[None] * y for i in range(0, x)] 

arr1 = two_d_array(2, 3)
arr1[0][0] = 5
print arr1
