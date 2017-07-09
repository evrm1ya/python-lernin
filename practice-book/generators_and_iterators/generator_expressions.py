# Generator expressions
# generator version of list comprehensions
# returns a generator instead of a list

import generator_notes

a  = (x * x for x in range(10))

print a
print sum(a)

# find first n pythagorean triplets
# `(x, y, z)` called pythagorean triplets
# if x*x + y*y == z*z

pyt = (
    (x, y, z) for z in generator_notes.integers()
    for y in xrange(1, z)
    for x in range(1, y)
    if x * x + y * y == z * z
)

print generator_notes.take(10, pyt)

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print line

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

main('dog', ['./a.txt', './b.txt'])

