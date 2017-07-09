# `iter` takes an iterable object and returns an iterator
x = iter([1, 2, 3])
print x.next()
print x.next()
print x.next()

# print x.next()
# raises StopIteration

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

a = yrange(3)
print a.next()
print a.next()
print a.next()

# print a.next()
# raises StopIteration

# behind the scenes the iter fn calls `__iter__` method on the given object
# return value of `__iter__` is an iterator
# should have a `next` method

# many built in fns accept iterators as args
print list(yrange(5))
print sum(yrange(5))

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

y = yrange(5)
print list(y)
print list(y)

z = zrange(5)
print list(z)
print list(z)

# Problem 1
# Write an iterator class `reverse_iter` that takes a list
# and iterates it from the reverse direction.

class reverse_iter:
    def __init__(self, l):
        self.i = len(l) - 1
        self.list = l

    def __iter__(self):
        return self

    def next(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return self.list[i]
        else:
            raise StopIteration()

it = reverse_iter([1, 2, 3, 4])
print it.next()
print it.next()
print it.next()
print it.next()

# print it.next()
# raises StopIteration

