# needs work for python3
for x in [1, 2, 3, 4, 5]:
    print x

for i in range(10):
    print i, i**2, i**3

names = ['a', 'b', 'c']
values = [1, 2, 3]

print(zip(names, values))

for name, value in zip(names, values):
    print name, value

# Problem 2:
# Python has a built-in function sum to find
# the sum of all elements of a list.
# Provide an implementation for sum.

def loop_sum(values):
    result = 0
    for x in values:
        result += x
    return result

print loop_sum(values)

def lambda_reduce_sum(values):
    return reduce(lambda x,y: x + y, values)

print lambda_reduce_sum(values)

def add(x, y):
    return x + y

def product(x, y):
    return x * y

def no_lambda_reduce_sum(values):
    return reduce(add, values)

print no_lambda_reduce_sum(values)

# Problem 3:
# Make the sum implementation work for strings as well.
# print sum(['hello', 'world'])
# => 'helloworld'
strings = ['hello', 'world']

print lambda_reduce_sum(strings)
print no_lambda_reduce_sum(strings)

# Problem 4:
# Implement a function `product` to compute
# the product of a list of numbers

def lol_reduce(fn):
    def f(items):
        return reduce(fn, items)
    return f

lol_sum = lol_reduce(lambda x,y: x + y)
lol_product = lol_reduce(lambda x,y: x * y)

print lol_sum([100, 200, 300])
print lol_product([3, 5, 7, 11, 17])
print lol_sum([100, 200, 300] + [lol_product([3, 5, 7, 11, 17])])

# Problem 5
# Write a function `factorial`
# Use the `product` function if possible
def factorial(num):
    return lol_product(range(1, num + 1))

print factorial(4)
print factorial(5)

# Problem 6
# Write a function reverse to reverse a list.
# Do it without list slicing.

reverse_numbers = [1, 2, 3, 4]

# meh
def such_reverse(numbers):
    result = []
    idx = -1
    for x in numbers:
        result.append(numbers[idx])
        idx = idx - 1
    return result

print such_reverse(reverse_numbers)
# doesn't mutate - yay!
print reverse_numbers
print such_reverse(such_reverse(reverse_numbers))

def such_reverse_much_wow(numbers):
    result = []
    idx = len(numbers)
    while idx > 0:
        result.append(numbers[idx - 1])
        idx = idx - 1
    return result

print such_reverse_much_wow(reverse_numbers)
print such_reverse_much_wow(such_reverse_much_wow(reverse_numbers))
print such_reverse_much_wow([])

# Problem 7
# Write custom `min` and `max` functions
# What happens when called with lists of strings?

min_max_numbers = [4, -1, -10, 8]
min_max_strings = ['z', 'a', 'e', 'p']

# assumes types of values are the same
def compare(fn):
    def f(values):
        result = values[0]
        for x in values[1:]:
            if fn(x, result):
                result = x
        return result
    return f

def isLessThan(x, y):
    return x < y

def _not(fn):
    def f(x, y):
        return not fn(x, y)
    return f

new_min = compare(isLessThan)
new_max = compare(_not(isLessThan))

print new_min(min_max_numbers)
print new_max(min_max_numbers)
print new_min(min_max_strings)
print new_max(min_max_strings)

# Problem 8
# Cumulative sum of a list
# [a, a+b, a+b+c, ...]
# Write an implementation

# Problem 9
# Cumulative product

def cumulative_math(fn):
    def f(values):
        result = [values[0]]
        for i, x in enumerate(values[1:]):
            result.append(fn(x, result[i]))
        return result
    return f

cumulative_sum = cumulative_math(add)
cumulative_product = cumulative_math(product)

print cumulative_sum([1, 2, 3, 4])
print cumulative_sum([4, 3, 2, 1])
print cumulative_product([1, 2, 3, 4])
print cumulative_product([4, 3, 2, 1])

# Problem 10
# Write a function `unique`to find all
# the unique elements of a list.

def unique(values):
    cache = {}
    result = []
    for x in values:
        if x in cache:
            continue
        cache[x] = 1
        result.append(x)
    return result

print unique([1, 2, 1, 3, 2, 5])

# Problem 11
# Implement `dups` to find all duplicates in a list.

def counts(values):
    counts = {}
    for x in values:
        if x in counts:
            counts[x] = counts[x] + 1
            continue
        counts[x] = 1
    return counts

print counts([1, 2, 1, 3, 2, 5])

def dups(values):
    result = []
    cache = counts(values)
    for key in cache:
        if cache[key] > 1:
            result.append(key)
    return result

print dups([1, 2, 1, 3, 2, 5])

# Problem 12
# Implement `group(list, size)` that takes a list
# and splits it into smaller lists of given size.

def group(l, size):
    result = []
    i = len(l) / size if len(l) % size == 0 else len(l) // size + 1
    start = 0
    end = size
    while i > 0:
        result.append(l[start:end])
        start = start + size
        end = end + size
        i = i - 1
    return result

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

