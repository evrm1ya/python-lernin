print(type(abs))

def apply_to_each(l, f):
    """
    Assumes l is a list, f a function
    Mutates l by replacing each element, e, of l by f(e)
    """
    for i in range(len(l)):
        l[i] = f(l[i])

l = [1, -2, 3.33]
apply_to_each(l, abs)
print('l =', l)

l1 = [1, 28, 36]
l2 = [2, 57, 9]
for i in map(min, l1, l2):
    print(i)

l3 = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
    l3.append(i)
print(l3)
