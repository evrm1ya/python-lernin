# newlines count
def charcount(filename):
    return len(open(filename).read())

print charcount('foo.txt')
print charcount('bar.txt')

def wordcount(filename):
    return len(open(filename).read().split())

print wordcount('foo.txt')
print wordcount('bar.txt')

def linecount(filename):
    return len(open(filename).readlines())

print linecount('foo.txt')
print linecount('bar.txt')
