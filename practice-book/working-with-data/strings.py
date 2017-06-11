print 'el' in 'hello'
print 'EL' in 'hello'

def includes(include, string, transform=None):
    if transform != None:
        return transform(include) in transform(string)
    return include in string

print includes('EL', 'hello', transform=lambda s: s.lower())

print ' hello world\n'.strip()

a = 'hello'
b = 'python'
print "%s %s" % (a, b)

# Problem 16
# Write a function `extsort` to sort a list
# of files based on extension.

def split_file(f):
    split = f.split('.')
    return split[1] + '.' + split[0]

def extsort(files):
    return sorted(files, key=split_file)

print extsort(['a.c', 'a.py', 'b.py', 'appy.py', 
    'bar.txt', 'foo.txt', 'txty.txt', 'x.c'])

