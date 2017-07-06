a = {'x': 1, 'y': 2, 'z': 3}

print a
print a['x']
print a['z']

b = {}
b['x'] = 2
b[2] = 'foo'
b[(1, 2)] = 3

print b
print b[(1, 2)]

del a['x']
print a

print b.keys()
print b.values()
print b.items()

for key in a: 
    print key

for k, v in b.items():
    print k, v

print 'x' in a
print 'a' in a

print a.has_key('x')
print b.has_key((1, 2))

d = {'x': 1, 'y': 2, 'z': 3}
print d.get('x', 5)

# default
print d.get('p', 5)
print d

d.setdefault('x', 0)
print d

d.setdefault('p', 0)
print d

print 'hello %(name)s' % {'name': 'python'}

e = {'index': 2, 'name': 'Data Structures'}
print 'Chapter %(index)d: %(name)s' % e
