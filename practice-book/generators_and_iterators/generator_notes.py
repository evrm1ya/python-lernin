# generators simplify creation of iterators
# generator
#   => a fn that produces a sequence of results instead
#      of a single value

# each time `yield` statement is executed
# the fn generates a new value.
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y = yrange(3)

print y.next()
print y.next()
print y.next()

# print y.next()
# raises StopIteration

# When a generator fn is called, it returns a generator object
# without beginning execution of the fn.
# When `next` is called the fn starts executing until it reaches
# the `yield` statement.
# Yielded value is returned by the `next` call.

def foo():
    print 'begin'
    for i in range(3):
        print 'before yield', i
        yield i
        print 'after yield', i
    print 'end'

f = foo()
f.next()
f.next()
f.next()
# f.next()

def integers():
    '''Infinite seq of integers.'''
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    '''Returns first n values from the given seq.'''
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares())
